from windrose import WindroseAxes
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
#from vector_mapping import *
import xarray as xr
from math import *
import array

# Make arrays for pollution concentrations and wind speeds
arr1 = np.array([])
arr3 = np.array([])
u=  np.array([])
v=  np.array([])

# Enter coordinates
y=60       # lat
x=6.25    # lon

# Location options
#y 30.0 30.5 31.0 31.5 32.0 ... 68.0 68.5 69.0 69.5 70.0
#x -30.0 -29.38 -28.75 -28.12 ... 48.12 48.75 49.38 50.0

#wind directions ____________________________________________________________________________________________________

# Select wind files of three days
dataDIR2 = 'C:/Python/Data/wind/07/MERRA2.20050720.A3dyn.05x0625.EU.nc4'
DS2 = xr.open_dataset(dataDIR2)

dataDIR3 = 'C:/Python/Data/wind/07/MERRA2.20050721.A3dyn.05x0625.EU.nc4'
DS3 = xr.open_dataset(dataDIR3)

dataDIR4 = 'C:/Python/Data/wind/07/MERRA2.20050722.A3dyn.05x0625.EU.nc4'
DS4 = xr.open_dataset(dataDIR4)

# Get wind speeds from file and add to array
U = DS2.U.sel(lat=y, lon=x, lev=1, method='nearest')
V = DS2.V.sel(lat=y, lon=x, lev=1, method='nearest')

u = np.append(u, U)
v = np.append(v, V)

U = DS3.U.sel(lat=y, lon=x, lev=1, method='nearest')
V = DS3.V.sel(lat=y, lon=x, lev=1, method='nearest')

u = np.append(u, U)
v = np.append(v, V)

U = DS4.U.sel(lat=y, lon=x, lev=1, method='nearest')
V = DS4.V.sel(lat=y, lon=x, lev=1, method='nearest')

u = np.append(u, U)
v = np.append(v, V)

# Calculate wind direction from speeds
#winddir = 180 + (180/pi) * np.arctan2(u,v)

winddir_over = 270 - np.arctan2(v, u) * 180/pi
winddir = np.mod(winddir_over,360)

print(u)
print(v)
print('this is winddir')
print(winddir)
print('this is not winddir anymore')

#concentrations_________________________________________________________________________________________-

# Open pollution file with aircraft pollution
dataDIR = '../data/PM25.1h.JUL.ON.nc4'
DS = xr.open_dataset(dataDIR)

# Get data set with right location and times from file
da=DS.PM25.sel(lat=y, lon=x, method='nearest')
da = da.sel(time=slice('2005-07-20T00:30:00.000000000', '2005-07-22T23:30:00.000000000'))

# Make array with average of 3 hours to match wind data
for i in range(24):
    a=(da[3*i]+da[3*i+1]+da[3*i+2])/3
    arr2=np.array([a])
    arr1=np.append(arr1,arr2)
print(arr1)

#_______________________________________________________________________

# Open pollution file without aircraft pollution
dataDIR = '../data/PM25.1h.JUL.OFF.nc4'
DS = xr.open_dataset(dataDIR)

da=DS.PM25.sel(lat=y, lon=x, method='nearest')

#print(DS.var)

da = da.sel(time=slice('2005-07-20T00:30:00.000000000', '2005-07-22T23:30:00.000000000'))

for i in range(24):
    a=(da[3*i]+da[3*i+1]+da[3*i+2])/3
    arr2=np.array([a])
    arr3=np.append(arr3,arr2)
    print(arr3)

#plotting__________________________________________________________________________________________________

# Make pollution concentration and wind direction arrays
ws = arr1 -arr3
wd = winddir

# Make wind rose plot
ax = WindroseAxes.from_ax()
ax.bar(wd, ws, nsector=8, normed=True, opening=0.8, edgecolor='white')
ax.set_legend()
plt.show()

