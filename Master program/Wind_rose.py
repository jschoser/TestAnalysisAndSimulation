from windrose import WindroseAxes
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
#from vector_mapping import *
import xarray as xr
from math import *
import array


arr1 = np.array([])

# single file
dataDIR = '../data/PM25.1h.JAN.ON.nc4'
DS = xr.open_dataset(dataDIR)

dataDIR2 = 'E:/pythion/pythion wind/01/MERRA2.20050131.A3dyn.05x0625.EU.nc4'
DS2 = xr.open_dataset(dataDIR2)

#dataset = netcdf_dataset('../Data/wind/' + month + '/MERRA2.2005' + month + day + '.A3dyn.05x0625.EU.nc4')

U=DS2.U.sel(lat=32.0, lon=48.12,lev=1, method='nearest')
V=DS2.V.sel(lat=32.0, lon=48.12,lev=1, method='nearest')

print(U)

#winddir = 180 + (180/pi) * atan2(V/U)


da=DS.PM25.sel(lat=32.0, lon=48.12, method='nearest')

print(da.var)

da = da.sel(time=slice('2005-01-20T00:30:00.000000000', '2005-01-22T23:30:00.000000000'))
for i in range(24):
    a=(da[3*i]+da[3*i+1]+da[3*i+2])/3
    arr2=np.array([a])
    arr1=np.append(arr1,arr2)
print(arr1)


ws = arr1
wd = np.random.random(24) * 360

# Make wind rose plot
ax = WindroseAxes.from_ax()
ax.bar(wd, ws, nsector=8, normed=True, opening=0.8, edgecolor='white')
ax.set_legend()

plt.show()

print(ws)
print(wd)
