import xarray as xr
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from Altitude_converter import altitude_to_eta

# ==================================== INPUT ============================================

# Select the altitude [km]
h = 0

# Enter the pollutant (Black Carbon ('BC') or Ozone ('O3'))
pollutant = 'BC'

# ======================================================================================

# Convert the altitude
h = altitude_to_eta(h)

# Names of the dataset to be loaded if black carbon is selected
if pollutant == 'BC':

    # Dataset name
    name_DS = 'Soot'

    # Pollutant
    name_poll = 'AerMassBC'

# Names of the dataset to be loaded if Ozone is selected
elif pollutant == 'O3':

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
summer = 0
for t in da_summer.time.values:
    summer += da_summer.sel(time=t)

summer = summer / da_summer.time.size

winter = 0
for t in da_winter.time.values:
    winter += da_winter.sel(time=t)

winter = winter / da_winter.time.size

# Calculate the percentage difference between winter and summer
da = 100 * winter / summer - 100

# Select the desired altitude
seasonal_dif = da.sel(lev=h, method='nearest')  # .sel(time='2005-1-17')[0] # select appropriate level (ground) and day

# select projection. Only seems to work with PlateCarree though
proj = ccrs.PlateCarree()

# create axes
ax = plt.axes(projection=proj)

# draw coastlines with given resolution
ax.coastlines(resolution='50m')

# Plot the result
seasonal_dif.plot(cmap='coolwarm', vmax=100, vmin=-100)

plt.show()
print("Done")