import xarray as xr
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from Altitude_converter import altitude_to_eta

# ==================================== INPUT ============================================

# Select the altitude [km]
h = 0

# Enter the pollutant (Black Carbon ('BC') or Ozone ('Ozone'))
pollutant = 'Ozone'

# =======================================================================================

# Convert the altitude
h = altitude_to_eta(h)

# Names of the dataset to be loaded if black carbon is selected
if pollutant == 'BC':

    # Dataset name
    name_DS = 'Soot'

    # Pollutant
    name_poll = 'AerMassBC'

# Names of the dataset to be loaded if Ozone is selected
elif pollutant == 'Ozone':

    # Dataset name
    name_DS = 'O3'

    # Pollutant
    name_poll = 'SpeciesConc_O3'

# Stop the program in case a non-supported pollutant was entered
else:
    print("Invalid Pollutant name")
    exit()

# Filepaths to datasets
filename_winter_on = "Data/" + name_DS + ".24h.JAN.ON.nc4"
filename_winter_off = "Data/" + name_DS + ".24h.JAN.OFF.nc4"

filename_summer_on = "Data/" + name_DS + ".24h.JUL.ON.nc4"
filename_summer_off = "Data/" + name_DS + ".24h.JUL.OFF.nc4"

# Extract data set from netCFD file
DS_winter_on = xr.open_dataset(filename_winter_on)
DS_winter_off = xr.open_dataset(filename_winter_off)

DS_summer_on = xr.open_dataset(filename_summer_on)
DS_summer_off = xr.open_dataset(filename_summer_off)

# retrieve data array containing 24h average concentrations (21 days) for aviation only
da_winter = getattr(DS_winter_on, name_poll) - getattr(DS_winter_off, name_poll)
da_summer = getattr(DS_summer_on, name_poll) - getattr(DS_summer_off, name_poll)

# Average the data over time (one month)
summer = da_summer.mean(dim = 'time')

winter = da_winter.mean(dim = 'time')

# Calculate the percentage difference between winter and summer
da = 100 * winter / summer - 100

# Select the desired altitude
seasonal_dif = da.sel(lev=h, method='nearest')

# select projection. Only seems to work with PlateCarree though
proj = ccrs.PlateCarree()

# create axes
ax = plt.axes(projection=proj)

# draw coastlines with given resolution
ax.coastlines(resolution='50m')

# Plot the result
im = seasonal_dif.plot.pcolormesh(ax=ax, cmap='coolwarm', vmax=200, vmin=-200, add_colorbar = False)

# Make a colorbar
cb = plt.colorbar(im, orientation="vertical", shrink = 0.55)

# Set axis size to avoid white edges
plt.axis([-27,47,33,67])

# This line sets an empty title, because otherwise xarray automatically sets
ax.set_title("")

# Show the plot
plt.show()