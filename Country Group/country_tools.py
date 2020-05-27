from collections import OrderedDict
import cartopy.io.shapereader as shpreader
from cartopy import crs
from shapely import geometry
import xarray as xr
import numpy as np
from matplotlib import pyplot as plt
from descartes import PolygonPatch
from pyproj import Geod, Transformer
import json
import pathlib

"""
Tools to analyse emission and pollution on a country level. For more explanation how to use them, check the other files
in this directory.

@author Jakob Schoser
"""

# different modes for plotting emission and/or pollution data
RETURN_RATIO = "Ground Pollution/Emission Ratio"
RETURN_EMISSIONS = "Emissions"
RETURN_POLLUTION = "Ground Pollution"
RETURN_BOTH = "Emissions and Ground Pollution"  # should not be used for map plots, but is useful for scatter plots

# different ways of to combine the data inside one country
METHOD_AVG = "Area weighted average"
METHOD_POP = "Multiplied by population"
METHOD_MEDIAN = "Median"

POLLUTION_COLLECTIONS = ["O3.24h", "Aerosol.24h", "Soot.24h"]

lon_range = [-28.12 - 0.625/2, 48.12 + 0.625/2]
lat_range = [31.5 - 0.5/2, 68.5 + 0.5/2]


# return the name of a cache file which was created using the same settings that the program is now run on. Will be used
# to look for such a file or create one if it doesn't already exist
def cache_filename(poll_coll, summer, poll_chem, em_chem, em_lev):
    return poll_coll + "_" + ("JUL" if summer else "JAN") + "_" + poll_chem + "_" + em_chem + "_" +\
           str(em_lev.start) + "_" + str(em_lev.stop)


# return a path object leading to the data directory
def data_dir():
    return pathlib.Path.cwd().parent / "Data"


# generate the name of a data file using the convention
def data_filename(poll_coll, summer, poll_on):
    return poll_coll + ".{}.{}.nc4".format("JUL" if summer else "JAN", "ON" if poll_on else "OFF")


# create a dictionary containing the polygons for all countries listed in "interesting". This function returns an
# ordered dictionary with the format "country_name: [[list of polygons that it is made up of], total area]"
def create_country_polygons(shapefile_path="Shapefiles/CNTR_RG_20M_2016_4326.shp",
                            country_list_filename="countries.json"):
    frame = geometry.Polygon([(lon_range[0], lat_range[0]), (lon_range[1], lat_range[0]), (lon_range[1], lat_range[1]),
                              (lon_range[0], lat_range[1])])  # the geographic area for which we have data
    geod = Geod('+a=6378137 +f=0.0033528106647475126')  # object used for conversion from degrees to km

    # read the shape file
    reader = shpreader.Reader(shapefile_path)

    # this is a generator, not a list. So you can only loop over it, not use indexing. But if necessary, it can be
    # converted using list( ).
    countries = reader.records()

    # list of all countries to be checked
    country_file = json.load(open(country_list_filename))

    # the keys are country names (in English), and the value for each of them is a list with the polygons that the
    # country shape is made up of
    country_poly = {}

    # fill the country_poly
    for country in countries:
        # the .split( ) part in this statement is necessary because for some reason the names have \x00\x00\x00... added
        # to them. If you don't remove that, the statement doesn't find any of them in the "interesting" list
        country_name = country.attributes['NAME_ENGL'].split("\x00")[0]
        if country_name in country_file:
            # create empty list which will be filled with the polygons of the country, and set total area to 0
            country_poly[country_name] = [[], 0]
            multipolygon = country.geometry.geoms  # a multipolygon can consist of several disjoint polygons
            for polygon in multipolygon:  # each of these is a shapely polygon
                # get the portion of the polygon that's inside the data frame. This may result in shapely polygons or
                # multipolygons being created (e.g. if the original polygon is split in half)
                inside_frame = polygon.intersection(frame)

                # function used to add a polygon to the dictionary
                def add_region(region):
                    country_poly[country_name][0].append(region)
                    # add the area of the country which lies inside of the frame (in km^2)
                    country_poly[country_name][1] += abs(geod.geometry_area_perimeter(region)[0] / 1E6)

                if isinstance(inside_frame, geometry.Polygon) and not inside_frame.is_empty:
                    add_region(inside_frame)

                elif isinstance(inside_frame, geometry.MultiPolygon) and not inside_frame.is_empty:
                    for region in inside_frame:  # loop over all the polygons that make up the multipolygon
                        add_region(region)

            # eliminate any countries that don't have any polygons inside of the data frame
            if not country_poly[country_name][0]:
                del country_poly[country_name]

    # return an ordered dictionary (countries in alphabetical order)
    return OrderedDict(sorted(country_poly.items(), key=lambda t: t[0]))


# find the name of the country in which the coordinates (lon, lat) lie. Return None if it does not lie inside any
# of the countries listed in "countries". "countries" has the same format as the return value of
# create_country_polygons(), i.e. a dictionary with country names as keys and lists of polygons as values
def find_country_name(country_polygons, lon, lat):
    for name in country_polygons:  # loop over all countries
        for region in country_polygons[name][0]:  # loop over each polygon that the country is made of
            if region.contains(geometry.Point(lon, lat)):  # check if the polygon contains the coordinates
                return name
    return None


# find the ground level pollution due to aircraft and aircraft emission data for each country, and return it
# in an ordered dictionary in the form "country_name: data". The data depends on the selected mode and can either be
# ground pollution, emissions or the ratio of the two. Also, these values can be calculated per country using an
# area-weighted average or by taking the median of all cells inside it
# The output units are;
#   - kg/m^2/day for emissions
#   - mu_g/m^3 for pollution (except ppbv for ozone)
#   - (mu_g/m^3) / (kg/m^2/day) for the ratio
def find_poll_em_data(country_polygons, poll_coll, em_chemical, poll_chemical, emission_levels, summer,
                      em_filename="AvEmFluxes.nc4", data_dir=pathlib.Path.cwd().parent / "Data",
                      recalculate_country_cells=False, country_cell_filename="country_cells.json", method=METHOD_AVG,
                      outliers=None, mode=RETURN_RATIO, pop_filename="Population.nc4"):

    em_filepath = data_dir / em_filename
    poll_on_filepath = data_dir / data_filename(poll_coll, summer, True)
    poll_off_filepath = data_dir / data_filename(poll_coll, summer, False)
    pop_filepath = data_dir / pop_filename

    DS = xr.open_dataset(em_filepath)
    da_em = getattr(DS, em_chemical) * 24 * 3600  # select only the specified emissions and convert to "per day"

    DS_on = xr.open_dataset(poll_on_filepath)
    DS_off = xr.open_dataset(poll_off_filepath)

    # subtract pollution data without aircraft from pollution with aircraft to retrieve the pollution caused by
    # aircraft only. Also, only select the appropriate chemical
    da_poll = getattr(DS_on, poll_chemical) - getattr(DS_off, poll_chemical)

    DS_pop = xr.open_dataset(pop_filepath)
    da_pop = DS_pop.pop

    poll_em_data = {}
    lon_axis = da_em.coords['lon'].values  # the longitude values of the data grid
    lat_axis = da_em.coords['lat'].values  # the latitude values of the data grid

    # geographic parameters used to estimate area of the grid cells as a function of latitude
    geod = Geod('+a=6378137 +f=0.0033528106647475126')

    if pathlib.Path(country_cell_filename).exists() and not recalculate_country_cells:
        with open(country_cell_filename) as file:
            country_cells = json.load(file)
        print("Retrieved list of cells per country from existing file")

    else:  # in case there is no cache file or the user wants to recalculate it
        country_cells = {}
        for lon in lon_axis:
            for lat in lat_axis:  # loop over all cells in the data grid
                country = find_country_name(country_polygons, lon, lat)  # find the country the cell lies in
                if country is not None:
                    if country not in country_cells:
                        country_cells[country] = []
                    country_cells[country].append([float(lon), float(lat)])
        with open(country_cell_filename, "w") as outfile:
            json.dump(country_cells, outfile, indent=4)

    # number of time steps in the pollution file
    poll_timesteps = len(da_poll.coords["time"].values)

    cell_areas = []  # list for the area of each cell inside a country. Only used as temporary storage

    # this block fills poll_em_data in the format "country_name: [total_emissions, time_averaged_pollution]"
    for country in country_cells:
        for cell in country_cells[country]:  # loop over all cells in the data grid
            if country not in poll_em_data:
                # if this is the first time the country is detected, set emission and pollution counters to 0
                poll_em_data[country] = [[], []]
                cell_areas = []

            # select the correct values from the simulation data and add it to the lists. Sum over all parameters
            # which are not explicitly specified (i.e. time in this case). Also select correct altitudes for both
            # emission and pollution. For pollution, divide by the number of time steps to get the time average
            cell_em = np.sum(da_em.sel(lon=cell[0], lat=cell[1], lev=emission_levels).values)
            cell_poll = np.sum(da_poll.sel(lon=cell[0], lat=cell[1], lev=1, method='nearest').values) / poll_timesteps

            if "O3" in poll_chemical:
                cell_poll *= 10 ** 9

            if method == METHOD_POP:  # TODO: is this really the best way of using it? (think of mode == RETURN_RATIO)
                cell_pop = da_pop.sel(lon=cell[0], lat=cell[1]).values
                cell_em *= cell_pop
                cell_poll *= cell_pop

            elif method == METHOD_AVG:
                # calculate area of the cell to make an area-weighted average of all cells in the country
                cell_lat_length = geod.line_length([cell[0], cell[0]], [cell[1] - 0.5/2, cell[1] + 0.5/2])
                cell_lon_length = geod.line_length([cell[0] - 0.625/2, cell[0] + 0.625/2], [cell[1], cell[1]])
                cell_areas.append(cell_lat_length * cell_lon_length)

            poll_em_data[country][0].append(cell_em)
            poll_em_data[country][1].append(cell_poll)

        if method == METHOD_AVG:
            # perform area-weighted average between the cells
            poll_em_data[country][0] = np.dot(poll_em_data[country][0], cell_areas) / sum(cell_areas)
            poll_em_data[country][1] = np.dot(poll_em_data[country][1], cell_areas) / sum(cell_areas)

        elif method == METHOD_MEDIAN:
            # calculate the median of emission and pollution values
            poll_em_data[country] = np.median(poll_em_data[country], axis=1)

        elif method == METHOD_POP:
            poll_em_data[country] = np.sum(poll_em_data[country], axis=1)

        else:
            print("Invalid averaging method:", method)

        if mode == RETURN_RATIO:
            if poll_em_data[country][0] != 0 and (outliers is None or country not in outliers):
                # divide pollution by emissions
                poll_em_data[country] = poll_em_data[country][1] / poll_em_data[country][0]
            else:  # remove the country from the data set if it is an outlier or if it has no emissions
                del poll_em_data[country]

        elif mode == RETURN_EMISSIONS or mode == RETURN_POLLUTION:
            if outliers is None or country not in outliers:
                # only keep the selected value
                poll_em_data[country] = poll_em_data[country][0 if mode == RETURN_EMISSIONS else 1]
            else:  # remove the country from the data set if it is an outlier
                del poll_em_data[country]

        elif mode != RETURN_BOTH:
            print("Error: Invalid mode:", mode)

    # check for any missing countries in the file
    requested_keys = set(country_polygons.keys())
    returned_keys = set(poll_em_data.keys())
    unavailable = list(requested_keys.difference(returned_keys))

    # return data, along with the names of all missing countries
    return OrderedDict(sorted(poll_em_data.items(), key=lambda t: t[0])), unavailable


# returns a matrix that gives the spatial correlation between countries (based on the inverse of the distance between
# them). Used for spatial autocorrelation measurement
def spatial_matrix(country_polygons):
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:3035")  # used to transform longitude and latitude to metres
    centres = []  # list for the centres of all countries
    for country in country_polygons:
        # the centre of the country is the weighted average of the centres of its sub-regions
        centre_lon_lat = sum([np.array(region.centroid) * region.area for region in country_polygons[country][0]]) / \
                         sum([region.area for region in country_polygons[country][0]])
        centres.append(transformer.transform(centre_lon_lat[0], centre_lon_lat[1]))  # transform centre to metres

    centres = np.array(centres) / 1E3  # convert centre coordinates from metres to kilometres
    polygon_values = list(country_polygons.values())  # values of the polygon list (used to get area of the country)
    w = np.zeros((len(country_polygons), len(country_polygons)))  # empty matrix for weights
    # loop over all rows of the matrix, each corresponding to a country
    for i in range(len(w)):
        # characteristic radius of the country (radius of a circle with the same area)
        char_rad = np.sqrt(polygon_values[i][1] / np.pi)

        distances = np.linalg.norm(centres[i] - centres, axis=1)  # distances from this country to all others
        distances[i] = 1  # avoid division by zero (distance from the country to itself is 0)

        # weight of each country is the inverse of its distance, multiplied by the current country's characteristic
        # radius This scaling is done because the influence of a big country at its borders is just as big as the
        # influence of a small country at its borders. If we didn't use this factor, the weight of the neighbouring
        # countries of a big country would be smaller, since they are further away from its centre.
        w[i] = 1 / distances * char_rad

        w[i, i] = 0  # set the weight of the current country w.r.t itself to 0

    return w


# return the global Moran's I for the data set. A positive value indicates that values are clustered, i.e. similar
# values are close to each other on the map (positive spatial auto correlation). A negative value means that similar
# values are far apart, and zero means that values are randomly distributed (negative spatial auto correlation)
def morans_i_global(country_polygons, data):
    w = spatial_matrix(country_polygons)

    data_values = list(data.values())
    mean = np.mean(data_values)
    s = 0
    for i in range(len(w)):
        for j in range(len(w[i])):
            s += w[i, j] * (data_values[i] - mean) * (data_values[j] - mean)

    return len(data_values) / np.sum(w) * s / np.var(data_values)


# return the Geary's C for the data set. A value between 0 and 1 indicates positive spatial auto correlation,
# a value larger than 1 shows negative spatial auto correlation. More sensitive to local scales than Moran's I
def gearys_c(country_polygons, data):
    w = spatial_matrix(country_polygons)

    data_values = list(data.values())
    s = 0
    for i in range(len(w)):
        for j in range(len(w[i])):
            s += w[i, j] * (data_values[i] - data_values[j]) ** 2

    return (len(data_values) - 1) * s / (2 * np.sum(w) * np.var(data_values))


# return the local Moran's I for each country in the data set. A positive value indicates that the country's value is
# similar to its neighbours, while a negative value shows that it is an outlier compared to its surroundings.
def morans_i_local(country_polygons, data):
    w = spatial_matrix(country_polygons)
    data_values = list(data.values())
    mean = np.mean(data_values)
    i_local = []
    for i in range(len(w)):
        var = np.mean(np.delete(data_values, i))
        s = 0
        for j in range(len(w[i])):
            s += w[i, j] * (data_values[j] - mean)
        i_local.append((len(w) - 1) / var * (data_values[i] - mean) * s / np.sum(w[i]))

    country_names = list(country_polygons.keys())
    return OrderedDict({country_names[i]: i_local[i] for i in range(len(w))})


# functions to map the values for each country between 0 and 1
def lin_mapping(val, min_val, max_val):
    return (val - min_val) / (max_val - min_val)


def sqrt_mapping(val, min_val, max_val):
    return np.sqrt((val - min_val) / (max_val - min_val))


def log_mapping(val, min_val, max_val):
    return np.log((val - min_val) / (max_val - min_val) + 1) / np.log(2)


def generate_sub_title(poll_chemical, em_chemical, summer, emission_levels, method, mode):
    chemical_decription = ("Pollution chemical: " + poll_chemical + " | ")\
        if mode == RETURN_RATIO or mode == RETURN_POLLUTION else ""
    chemical_decription += ("Emission chemical: " + em_chemical + " | ")\
        if mode == RETURN_RATIO or mode == RETURN_EMISSIONS else ""
    if mode != RETURN_BOTH:
        chemical_decription += "Units: " + ("$\mu g/m^3$" if poll_chemical != "SpeciesConc_O3" else
                                             "ppbv") if mode != RETURN_EMISSIONS else ""
        chemical_decription += " / (" if mode == RETURN_RATIO else ""
        chemical_decription += "$kg/m^2/day$" if mode != RETURN_POLLUTION else ""
        chemical_decription += (")" if mode == RETURN_RATIO else "") + " | "
    return chemical_decription + "Time frame for pollution: " + ("July" if summer else "January") +\
           " 2005 | " + (("Altitude levels for emission: " + str(emission_levels.start) + " to " +
           str(emission_levels.stop) + " | ") if mode != RETURN_POLLUTION else "") + "Averaging method: " + method


# show map with colour coding for the pollution and/or emission data
def plot_map(country_polygons, processed_data, mode, poll_chemical, em_chemical, summer, emission_levels, method,
             add_title="", add_info="", show_removed=False, mapping=lin_mapping, colormap="coolwarm",
             removed_color=(0, 0, 0, 1), show_cells=False, vmax=None, vmin=None, show_title=True):

    # title for the entire plot
    if show_title:
        plt.suptitle(mode + add_title + "\n\n" +
                     generate_sub_title(poll_chemical, em_chemical, summer, emission_levels, method, mode))

    ax = plt.axes([0.05, 0.05, 0.8, 0.85])  # subplot for the map. [left, bottom, width, height]

    countries_with_poly = set(country_polygons.keys())
    countries_with_data = set(processed_data.keys())
    removed_countries = list(countries_with_poly.difference(countries_with_data))
    if show_removed:
        ax.set_xlabel("Removed countries: " + str(removed_countries) + "\n" + add_info)
    else:
        ax.set_xlabel(add_info)

    # only display the region for which we have data
    ax.set_xlim([lon_range[0], lon_range[1]])
    ax.set_ylim([lat_range[0], lat_range[1]])
    plt.tight_layout()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    # find maximum and minimum value to scale the colour coding
    min_val = min(processed_data.values()) if vmin is None else vmin
    max_val = max(processed_data.values()) if vmax is None else vmax

    # loop over all countries for which we have found a pollution and emission data. These are not necessarily the
    # same countries as the ones in the polygon dictionary, since some countries (e.g. Vatican City) are too small
    # to contain any data (the grid is too coarse). These countries will then not be plotted
    for name in processed_data:
        value = processed_data[name]  # retrieve the value for this country

        # select the colour based on the value. Nonlinear mappings can be used to make differences more apparent
        colour = plt.get_cmap(colormap)(mapping(value, min_val, max_val))
        for region in country_polygons[name][0]:  # loop over all regions that the country consists of
            ax.plot(*region.exterior.xy, alpha=0)  # plot the borders of the polygon
            ax.add_patch(PolygonPatch(region, facecolor=colour))  # fill the polygon with colour

    for name in removed_countries:
        for region in country_polygons[name][0]:  # loop over all regions that the country consists of
            ax.plot(*region.exterior.xy, alpha=0)  # plot the borders of the polygon
            ax.add_patch(PolygonPatch(region, facecolor=removed_color))  # fill the polygon with colour

    if show_cells:
        plot_grid()

    # create the colour legend
    plt.rcParams.update({'font.size': 26})
    legend_ax = plt.axes([0.9, 0.1, 0.05, 0.75])
    legend_ax.ticklabel_format(style='sci', axis='both', scilimits=(0,0), useOffset=False)
    gradient = mapping(np.linspace(min_val, max_val, 256), min_val, max_val).reshape(256, 1)[::-1]
    legend_ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(colormap), extent=[0, 1, min_val, max_val])
    legend_ax.xaxis.set_visible(False)


def plot_grid(country_cell_filename="country_cells.json"):
    if pathlib.Path(country_cell_filename).exists():
        with open(country_cell_filename) as file:
            country_cells = json.load(file)

    colours = plt.get_cmap("hsv")(np.linspace(0, 1, len(country_cells)))
    for country, c in zip(country_cells, colours):
        colour = np.random.rand() * np.ones(len(country_cells[country]))
        plt.scatter(np.array(country_cells[country])[:, 0], np.array(country_cells[country])[:, 1], c=[c], zorder=10)


def plot_high_res_map(poll_coll, em_chemical, poll_chemical, emission_levels, summer, mode,
                      em_filename="AvEmFluxes.nc4", data_dir=pathlib.Path.cwd().parent / "Data", add_title="",
                      colormap="coolwarm", mult_pop=False, vmax=None, vmin=None, pop_filename="Population.nc4"):

    em_filepath = data_dir / em_filename
    poll_on_filepath = data_dir / data_filename(poll_coll, summer, True)
    poll_off_filepath = data_dir / data_filename(poll_coll, summer, False)
    pop_filepath = data_dir / pop_filename

    DS = xr.open_dataset(em_filepath)
    da_em = getattr(DS, em_chemical).sel(lev=emission_levels).sum(dim='lev') * 24 * 3600  # select only the specified emissions and convert to "per day"

    DS_on = xr.open_dataset(poll_on_filepath)
    DS_off = xr.open_dataset(poll_off_filepath)

    # subtract pollution data without aircraft from pollution with aircraft to retrieve the pollution caused by
    # aircraft only. Also, only select the appropriate chemical
    da_poll = (getattr(DS_on, poll_chemical) - getattr(DS_off, poll_chemical)).sel(lev=1, method='nearest')

    # number of time steps in the pollution file
    poll_timesteps = len(da_poll.coords["time"].values)
    da_poll = da_poll.sum(dim='time') / poll_timesteps

    DS_pop = xr.open_dataset(pop_filepath)
    da_pop = DS_pop.pop

    if mode == RETURN_POLLUTION:
        da_data = da_poll
    elif mode == RETURN_EMISSIONS:
        da_data = da_em
    elif mode == RETURN_RATIO:  # doesn't work. Grid not the same!
        da_data = da_poll / da_em
    else:
        print("Invalid mode")
        return

    if mult_pop:
        da_data *= da_pop / 1E6  # does this make sense when the mode is RETURN_RATIO?

    proj = crs.PlateCarree()
    ax = plt.axes(projection=proj)
    ax.coastlines(resolution='50m')
    ax.set_title(mode + add_title + "\n\n" + generate_sub_title(poll_chemical, em_chemical, summer, emission_levels,
                                                            "High res", mode))

    da_data.plot(cmap=colormap, vmin=vmin, vmax=vmax)


# find the ground level pollution due to aircraft and aircraft emission data for each country, and return it
# in an ordered dictionary in the form "country_name: data". The data depends on the selected mode and can either be
# ground pollution, emissions or the ratio of the two. Also, these values can be calculated per country using an
# area-weighted average or by taking the median of all cells inside it
# The output units are;
#   - kg/m^2/day for emissions
#   - mu_g/m^3 for pollution (except ppbv for ozone)
#   - (mu_g/m^3) / (kg/m^2/day) for the ratio
def find_matrix_data(poll_colls, emission_levels, summer,
                    em_filename="AvEmFluxes.nc4", data_dir=pathlib.Path.cwd().parent / "Data",
                    country_cell_filename="country_cells.json", method=METHOD_AVG):

    em_filepath = data_dir / em_filename
    poll_on_filepaths = []
    poll_off_filepaths = []

    for poll_coll in poll_colls:
        poll_on_filepaths.append(data_dir / data_filename(poll_coll, summer, True))
        poll_off_filepaths.append(data_dir / data_filename(poll_coll, summer, False))

    print("Make sure that the 'names' array is in the same order as this")
    DS = xr.open_dataset(em_filepath)
    em_chemicals = DS.variables
    em_das = []
    for em_chemical in em_chemicals:
        # select only the specified emissions and convert to "per day"
        if em_chemical not in DS.coords:
            print(em_chemical)
            em_das.append(getattr(DS, str(em_chemical)) * 24 * 3600)

    poll_das = []
    for poll_on_filepath, poll_off_filepath in zip(poll_on_filepaths, poll_off_filepaths):
        DS_on = xr.open_dataset(poll_on_filepath)
        DS_off = xr.open_dataset(poll_off_filepath)
        poll_chemicals = DS_on.variables
        for poll_chemical in poll_chemicals:
            if poll_chemical not in DS_on.coords:
                print(poll_chemical)
                poll_das.append(getattr(DS_on, str(poll_chemical)) - getattr(DS_off, str(poll_chemical)))

    poll_em_data = {}

    # geographic parameters used to estimate area of the grid cells as a function of latitude
    geod = Geod('+a=6378137 +f=0.0033528106647475126')

    if pathlib.Path(country_cell_filename).exists():
        with open(country_cell_filename) as file:
            country_cells = json.load(file)
        print("Retrieved list of cells per country from existing file")

    else:  # in case there is no cache file or the user wants to recalculate it
        print("Error: no file with cell coordinates found")
        return None

    # number of time steps in the pollution file
    poll_timesteps = 21

    cell_areas = []  # list for the area of each cell inside a country. Only used as temporary storage

    # this block fills poll_em_data in the format "country_name: [total_emissions, time_averaged_pollution]"
    for country in country_cells:
        for cell in country_cells[country]:  # loop over all cells in the data grid
            if country not in poll_em_data:
                # if this is the first time the country is detected, set emission and pollution counters to 0
                poll_em_data[country] = [[] for _ in range(len(em_das) + len(poll_das))]
                cell_areas = []

            for i in range(len(em_das)):
                poll_em_data[country][i].append(np.sum(em_das[i].sel(lon=cell[0], lat=cell[1],
                                                                     lev=emission_levels).values))

            for j in range(len(poll_das)):
                poll_em_data[country][len(em_das) + j].append(np.sum(poll_das[j].sel(lon=cell[0], lat=cell[1], lev=1,
                                                                                     method='nearest').values) /
                                                              poll_timesteps)

            # calculate area of the cell to make an area-weighted average of all cells in the country
            cell_lat_length = geod.line_length([cell[0], cell[0]], [cell[1] - 0.5/2, cell[1] + 0.5/2])
            cell_lon_length = geod.line_length([cell[0] - 0.625/2, cell[0] + 0.625/2], [cell[1], cell[1]])
            cell_areas.append(cell_lat_length * cell_lon_length)

        if method == METHOD_AVG:
            # perform area-weighted average between the cells
            for param in range(len(poll_em_data[country])):
                poll_em_data[country][param] = np.dot(poll_em_data[country][param], cell_areas) / sum(cell_areas)

        elif method == METHOD_MEDIAN:
            # calculate the median of emission and pollution values
            poll_em_data[country] = np.median(poll_em_data[country], axis=1)

        else:
            print("Invalid averaging method:", method)

    # return data
    return OrderedDict(sorted(poll_em_data.items(), key=lambda t: t[0]))
