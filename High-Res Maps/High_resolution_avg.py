import xarray as xr
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# =================================================== Input ============================================================

# Choose the season
season = 'Summer'

# Choose the pollutant
pollutant = 'Ozone'

# ============================================ Loading the datafile ====================================================

# Datafile to be loaded
Name_DF = (pollutant == 'BC') * 'Soot' + (pollutant == 'Ozone') * 'O3'

# Get the name of the part of the dataset to be loaded
Name_DS = (pollutant == 'BC') * 'AerMassBC' + (pollutant == 'Ozone') * 'SpeciesConc_O3'

# Get the season
Season_DF = (season == 'Summer') * 'JUL' + (season == 'Winter') * 'JAN'


# Create the file paths based on the pollutants selected
filepath_on     = 'Data/' + Name_DF + '.24h.' + Season_DF + '.ON' + '.nc4'
filepath_off    = 'Data/' + Name_DF + '.24h.' + Season_DF + '.OFF' + '.nc4'

# Open datafiles with aviation on and off
DF_av_on    = xr.open_dataset(filepath_on)
DF_av_off   = xr.open_dataset(filepath_off)

# Subtract datafiles to isolate aviation-attributable pollution
DF_av_only = DF_av_on - DF_av_off


# ====================================== Selecting and averaging pollutants ============================================

# Selecting the dataset containing the desired pollutant
DS = getattr(DF_av_only, Name_DS)

# Averaging the pollutants over one month
DS_avg = DS.mean(dim = 'time')

# Select pollutant data at ground level
DS_avg_grd = DS_avg.sel(lev = 1, method = 'nearest')

# ============================================ Detecting outliers ======================================================

# Calculate the first and third quartile
Q1      = DS_avg_grd.quantile(.25)
Q3      = DS_avg_grd.quantile(.75)

# Calculate the interquartile range
IQR     = Q3 - Q1

# Calculate limits for outliers
# the bounds for vmax are greater than the standard 1.5 when BC is selected,
# but otherwise all of central Europe was seen as an outlier
vmin    = Q1 - (1.5*IQR)
vmax    = Q3 + ((1.5 + 1.5*(pollutant == 'BC'))*IQR)

# ============================================= Plotting Results =======================================================

# select projection. Only seems to work with PlateCarree though
proj = ccrs.PlateCarree()

# create axes
ax = plt.axes(projection=proj)

# draw coastlines with given resolution
ax.coastlines(resolution='50m')

# Plot the result
im = DS_avg_grd.plot.pcolormesh(ax=ax, cmap='coolwarm',
                                vmax = vmax,
                                vmin = vmin,
                                add_colorbar = False)

# Make a colorbar
cb = plt.colorbar(im, orientation="vertical", shrink = 0.55)

# Set axis size to avoid white edges
plt.axis([-27, 47, 33, 67])

# This line sets an empty title, because otherwise xarray automatically sets
ax.set_title("")

# Show the plot
plt.show()
