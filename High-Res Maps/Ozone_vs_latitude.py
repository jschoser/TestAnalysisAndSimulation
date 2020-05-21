import xarray as xr
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from Country_reader import Europe_Coordinates
import numpy as np
# =================================================== Input ============================================================

# Choose the season
season = 'Winter'

# Choose the pollutant
pollutant = 'Ozone'

# ============================================ Loading the datafile ====================================================

# Datafile to be loaded
Name_DF = (pollutant == 'BC') * 'Aerosol' + (pollutant == 'Ozone') * 'O3'

# Get the name of the part of the dataset to be loaded
Name_DS = (pollutant == 'BC') * 'PM25' + (pollutant == 'Ozone') * 'SpeciesConc_O3'



# Get the season
Season_DF = (season == 'Summer') * 'JUL' + (season == 'Winter') * 'JAN'


# Create the file paths based on the pollutants selected
filepath_on     = 'Data/' + Name_DF + '.24h.' + Season_DF + '.ON' + '.nc4'
filepath_off    = 'Data/' + Name_DF + '.24h.' + Season_DF + '.OFF' + '.nc4'

# Open datafiles with aviation on and off
DF_av_on    = xr.open_dataset(filepath_on)
DF_av_off   = xr.open_dataset(filepath_off)


# Subtract datafiles to isolate aviation-attributable pollution
DF_av_only = (DF_av_on - DF_av_off)

# ================================ Importing the grid cells of continental Europe ======================================

europe = Europe_Coordinates()

# ====================================== Selecting and averaging pollutants ============================================

# Selecting the dataset containing the desired pollutant
DS = getattr(DF_av_only, Name_DS)

# Averaging the pollutants over one month
DS_avg = DS.mean(dim = 'time')#.mean(dim = 'lon')

# Select pollutant data at ground level
DS_avg_grd = DS_avg.sel(lev = 1, method = 'nearest')

europe = europe[europe[:, 1].argsort()]


last_lat = 0
lat_sum = 0
distribution = []
n = 1
# Iterate through all points of continental Europe
for i in europe:
    # Reset sum and append values to a list at a new latitude
    if i[1] != last_lat:
        print(i[1])
        last_lat = i[1]
        distribution.append([last_lat, lat_sum/n])
        lat_sum = 0
        n = 0

    lat_sum += float(DS_avg_grd.sel(lat = i[1], method = 'nearest').sel(lon = i[0], method = 'nearest'))
    n += 1




# ============================================= Plotting Results =======================================================
distribution = np.array(distribution)

#DS_avg_grd.plot()
plt.plot(distribution[1:,0], distribution[1:,1])
plt.title("")

plt.xlabel("Latitude")

plt.ylabel("Ozone Average Dry Mixing Ratio")
plt.show()
