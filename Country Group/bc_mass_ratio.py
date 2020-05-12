import country_tools as ct
import xarray as xr
from pyproj import Geod

summer = False

poll_coll = "Soot.24h"  # the collection name for pollution (first part of the .nc4 filename)

# the chemicals to be taken into account for pollution and emissions, respectively. These need to be the names of the
# data sets inside the .nc4 files you selected
poll_chemical = "AerMassBC"
em_chemical = "NO2"

poll_av_on_filepath = ct.data_dir() / ct.data_filename(poll_coll, summer, True)
poll_av_off_filepath = ct.data_dir() / ct.data_filename(poll_coll, summer, False)
em_filepath = ct.data_dir() / "AvEmFluxes.nc4"

poll_av_on_DS = xr.open_dataset(poll_av_on_filepath)
poll_av_off_DS = xr.open_dataset(poll_av_off_filepath)
em_DS = xr.open_dataset(em_filepath)

poll_da = getattr(poll_av_on_DS, poll_chemical) - getattr(poll_av_off_DS, poll_chemical)
em_da = getattr(em_DS, em_chemical)

poll_da = poll_da.sel(lev=1, method='nearest').sum(dim='time') / 21
em_da = em_da.sel(lev=slice(0, 8)).sum(dim='lev')

lon_range = em_da.coords['lon'].values
lat_range = em_da.coords['lat'].values

geod = Geod('+a=6378137 +f=0.0033528106647475126')
polygons = ct.create_country_polygons()

tot_em = 0
tot_poll = 0
tot_area = 0

for lon in lon_range:
    for lat in lat_range:
        cell_lat_length = geod.line_length([lon, lon], [lat - 0.5 / 2, lat + 0.5 / 2])
        cell_lon_length = geod.line_length([lon - 0.625 / 2, lon + 0.625 / 2], [lat, lat])

        tot_em += (em_da.sel(lon=lon, lat=lat) * 3600 * 24 * cell_lon_length * cell_lat_length * 1E9).values
        # if ct.find_country_name(polygons, lon, lat) in ["Ireland", "United Kingdom", "Spain", "Portugal", "France",
        #                                                 "Belgium", "Luxemburg", "Germany", "Netherlands", "Iceland",
        #                                                 "Norway", "Switzerland", "Italy", "Faroes", "Austria", "Denmark"]:
        #     tot_poll += (poll_da.sel(lon=lon, lat=lat) * cell_lon_length * cell_lat_length).values
        #     tot_area += cell_lon_length * cell_lat_length


print(tot_em/1E9)
# print(tot_poll / tot_area)
