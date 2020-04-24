from windrose import WindroseAxes
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
#from vector_mapping import *
import xarray as xr

# single file
dataDIR = '../data/PM25.1h.JAN.ON.nc4'
DS = xr.open_dataset(dataDIR)

dataDIR2 = 'E:/pythion/pythion wind/01/MERRA2.20050131.A3dyn.05x0625.EU.nc4'
DS2 = xr.open_dataset(dataDIR2)

#dataset = netcdf_dataset('../Data/wind/' + month + '/MERRA2.2005' + month + day + '.A3dyn.05x0625.EU.nc4')

#X, Y = unpack_posdata()
#U, V = unpack_veldata(0)

# Create wind speed and direction variables

ws = np.random.random(200) * 6
wd = np.random.random(200) * 360

# Make wind rose plot
ax = WindroseAxes.from_ax()
ax.bar(wd, ws, nsector=8, normed=True, opening=0.8, edgecolor='white')
ax.set_legend()

plt.show()

#da=DS.PM25.variables#.sel(lat=32, lon=48.12, time='2005-01-22T23:30:00')
#da=DS.PM25.sel(lat=32, lon=48.12).sel(lev=1, method='nearest').sel(time='2005-1-22')
da=DS.PM25.sel(time='2005-01-22T23:30:00', lat=32.0, lon=48.12, method='nearest')
print('hey')
print(DS.lon.values)
print('hey')
#print(DS.PM25.values)
