from matplotlib import pyplot as plt
import country_tools as ct
from pprint import PrettyPrinter

"""
Shows map with colour coding for different statistics relating to aircraft emissions and ground pollution due to
aircraft. The available statistics for a selected pair of emission-pollution chemicals are:
    - Emissions of aircraft summed over a specified altitude range
    - Ground pollution due to aircraft summed over 21 days (January or July)
    - Ratio of ground pollution to emissions due to aviation
In order to obtain a single value for the country, several methods of combining the per-grid-cell data are supported:
    - Area average, which sums the data over the entire area of the country and then divides by its surface area
    - Median, which takes the median of all values in the country
The user can select between summer and winter using a boolean and define the altitude ranges over which emissions are
considered (e.g. to separate cruise and LTO emissions). In addition to that, outlier countries can be specified to make
local differences more visible. Countries who cause a division by zero during the calculation (e.g. if the emissions
are zero in the ratio statistic) will automatically be removed. All removed countries are shown in black.

In addition to a map displaying the data per country, the program outputs three indicators of spatial auto correlation:
Geary's C and global and local Moran's I. Global statistics are printed as a single value, while local statistics are
shown in a map

@author Jakob Schoser
"""

# Always keep in mind that the data for countries such as Russia and Algeria are only representative of the part of that
# country which lies within the data region (and not of the entire country)
# Also note that the pollution data is not influenced by areas outside of the data region (so the data does not show
# pollution caused in Western Europe by cruise emissions in the US)
# The numbers for emissions are often VERY small, in the order of 10^-14 to 10^-15. Be aware of machine precision
# AvEmMasses.nc4 can also be used instead of AvEmFluxes.nc4, but it does not contain any information about differences
# in altitudes. It merely contains the sum of all emissions over a certain grid cell

summer = False   # used to select between pollution data for January and July

poll_coll = "SOOT.24h"  # the collection name for pollution (first part of the .nc4 filename)

# the chemicals to be taken into account for pollution and emissions, respectively. These need to be the names of the
# data sets inside the .nc4 files you selected
poll_chemical = "AerMassBC"
em_chemical = "BC"

# the altitude levels over which emissions will be considered (available from 0 to 32). Check Altitude_levels.txt for
# conversion to km. Level 8: 1 km altitude, level 32: 13 km altitude
emission_levels = slice(0, 32)

# these countries will be ignored in the calculation. That is useful if some countries have such high or low values that
# they make it impossible to see any differences between the other countries
outliers = []  # ["Iraq", "Israel", "Latvia"]

mode = ct.RETURN_RATIO  # the statistic which is plotted (emissions, pollution or ratio between them)
method = ct.METHOD_AVG  # the way that the data is combined inside one country (median or area-weighted average)

do_spatial_analysis = False  # whether a second figure with spatial autocorrelation indicators should be displayed

colormap = "coolwarm"  # the color map used. Google "matplotlib color maps" to see the options

vmin, vmax = None, None  # extremes of the colour legend. If set to None, they are automatically chosen

mapping = ct.sqrt_mapping  # the mapping from values to the colour map. See country_tools for options


# ================= NO NEED TO CHANGE THINGS BELOW HERE (USUALLY) ==================

print("Creating country polygons...")
countries = ct.create_country_polygons()
countries_with_data = countries.copy()  # the countries which can be used for analysis later on

print("Retrieving pollution and emission data...")
data, unavailable = ct.find_poll_em_data(countries, poll_coll, em_chemical, poll_chemical, emission_levels, summer,
                                         mode=mode, outliers=outliers, method=method)
for country in unavailable:
    del countries_with_data[country]



print("Plotting the data...")
ct.plot_map(countries, data, mode, poll_chemical, em_chemical, summer, emission_levels, method,
            mapping=mapping, colormap=colormap, vmax=vmax, vmin=vmin)

moran_global, geary, moran_local = None, None, None

if do_spatial_analysis:
    print("Performing spatial analysis...")
    moran_global = ct.morans_i_global(countries_with_data, data)
    geary = ct.gearys_c(countries_with_data, data)
    moran_local = ct.morans_i_local(countries_with_data, data)

    print("Plotting the results of the spatial analysis...")
    plt.figure()
    ct.plot_map(countries, moran_local, mode, poll_chemical, em_chemical, summer, emission_levels, method,
                add_title=" (Local Moran's I)", add_info="Global Moran's I: " + str(moran_global) +
                                                         "\nGeary's C: " + str(geary), colormap=colormap,
                mapping=mapping)

print("Finished.\n")

pp = PrettyPrinter(indent=4)
print("============= RESULTS ==============\n")

print("These countries had no data available:", unavailable)
print("Data:")
pp.pprint(sorted(data.items(), key=lambda item: item[1]))

if do_spatial_analysis:
    print("Global Moran's I: ", moran_global)
    print("Geary's C: ", geary)
    print("Local Moran's I:")
    pp.pprint(moran_local)

plt.show()
