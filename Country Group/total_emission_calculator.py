import country_tools as ct
import xarray as xr
from pyproj import Geod

em_filepath = ct.data_dir() / "AvEmFluxes.nc4"
em_DS = xr.open_dataset(em_filepath)
em_da = em_DS.FUELBURN

fem_filepath = ct.data_dir() / "AvEmMasses.nc4"
fem_DS = xr.open_dataset(fem_filepath)
fem_da = fem_DS.FUELBURN

lon_range = em_da.coords['lon'].values
lat_range = em_da.coords['lat'].values

geod = Geod('+a=6378137 +f=0.0033528106647475126')

tot_fuelburn = 0

for lon in lon_range:
    for lat in lat_range:
        cell_lat_length = geod.line_length([lon, lon], [lat - 0.5 / 2, lat + 0.5 / 2])
        cell_lon_length = geod.line_length([lon - 0.625 / 2, lon + 0.625 / 2], [lat, lat])
        tot_fuelburn += (em_da.sel(lon=lon, lat=lat).sum(dim='lev') * 3600 * 24 * 365 * cell_lon_length *
                         cell_lat_length).values

print("with levels:", tot_fuelburn/1E9)
print("without levels:", fem_da.sum().values * 365/1E9)

