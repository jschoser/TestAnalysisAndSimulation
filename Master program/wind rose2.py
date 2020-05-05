from windrose import WindroseAxes
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
# from vector_mapping import *
import xarray as xr
from math import *
import array
import windrose

# Enter middle coordinate
y_mid = 40.5  # lat
x_mid = -3.56 # lon
# Location options
# y 30.0 30.5 31.0 31.5 32.0 ... 68.0 68.5 69.0 69.5 70.0
# x -30.0 -29.38 -28.75 -28.12 ... 48.12 48.75 49.38 50.0

fig = plt.figure()

# for loop for the 8 necessary plots
for k in range(8):
    # Coordinates
    if k == 0:
        y = y_mid + 0.5
        x = x_mid - 0.625
    elif k == 1:
        y = y_mid + 0.5
        x = x_mid
    elif k == 2:
        y = y_mid + 0.5
        x = x_mid + 0.625
    elif k == 3:
        y = y_mid
        x = x_mid + 0.625
    elif k == 4:
        y = y_mid - 0.5
        x = x_mid + 0.625
    elif k == 5:
        y = y_mid - 0.5
        x = x_mid
    elif k == 6:
        y = y_mid - 0.5
        x = x_mid - 0.625
    elif k == 7:
        y = y_mid
        x = x_mid - 0.625

    # Make arrays for pollution concentrations and wind speeds
    arr1 = np.array([])
    arr3 = np.array([])
    arr7 = np.array([])
    arr8 = np.array([])
    u = np.array([])
    v = np.array([])

    # wind directions ____________________________________________________________________________________________________

    # Select wind files of three days
    dataDIR2 = 'E:/pythion/pythion wind/07/MERRA2.20050711.A3dyn.05x0625.EU.nc4'
    DS2 = xr.open_dataset(dataDIR2)

    dataDIR3 = 'E:/pythion/pythion wind/07/MERRA2.20050712.A3dyn.05x0625.EU.nc4'
    DS3 = xr.open_dataset(dataDIR3)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050713.A3dyn.05x0625.EU.nc4'
    DS4 = xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050714.A3dyn.05x0625.EU.nc4'
    DS5 = xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050715.A3dyn.05x0625.EU.nc4'
    DS6 = xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050716.A3dyn.05x0625.EU.nc4'
    DS7 = xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050717.A3dyn.05x0625.EU.nc4'
    DS8 = xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050718.A3dyn.05x0625.EU.nc4'
    DS9 = xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050719.A3dyn.05x0625.EU.nc4'
    DS10 = xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050720.A3dyn.05x0625.EU.nc4'
    DS11= xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050721.A3dyn.05x0625.EU.nc4'
    DS12= xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050722.A3dyn.05x0625.EU.nc4'
    DS13= xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050723.A3dyn.05x0625.EU.nc4'
    DS14= xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050724.A3dyn.05x0625.EU.nc4'
    DS15= xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050725.A3dyn.05x0625.EU.nc4'
    DS16= xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050726.A3dyn.05x0625.EU.nc4'
    DS17= xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050727.A3dyn.05x0625.EU.nc4'
    DS18= xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050728.A3dyn.05x0625.EU.nc4'
    DS19 = xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050729.A3dyn.05x0625.EU.nc4'
    DS20= xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050730.A3dyn.05x0625.EU.nc4'
    DS21= xr.open_dataset(dataDIR4)

    dataDIR4 = 'E:/pythion/pythion wind/07/MERRA2.20050731.A3dyn.05x0625.EU.nc4'
    DS22= xr.open_dataset(dataDIR4)

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

    U = DS5.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS5.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS6.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS6.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS7.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS7.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS8.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS8.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS9.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS9.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS10.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS10.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS11.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS11.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS12.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS12.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS13.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS13.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS14.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS14.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS15.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS15.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS16.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS16.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS17.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS17.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS18.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS18.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS19.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS19.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS20.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS20.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS21.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS21.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    U = DS22.U.sel(lat=y, lon=x, lev=1, method='nearest')
    V = DS22.V.sel(lat=y, lon=x, lev=1, method='nearest')

    u = np.append(u, U)
    v = np.append(v, V)

    for i in range(21):
        a = (u[8 * i] + u[8 * i + 1]+u[8 * i + 2]+u[8 * i + 3]+u[8 * i + 4]+u[8 * i + 5]+u[8 * i + 6]+u[8 * i + 7])
        arr2 = np.array([a])
        arr7 = np.append(arr7, arr2)

    for i in range(21):
        a = (v[8 * i] + v[8 * i + 1]+v[8 * i + 2]+v[8 * i + 3]+v[8 * i + 4]+v[8 * i + 5]+v[8 * i + 6]+v[8 * i + 7])
        arr2 = np.array([a])
        arr8 = np.append(arr8, arr2)


    # Calculate wind direction from speeds

    # winddir = 180 + (180/pi) * np.arctan2(u,v)
    winddir_over = 270 - np.arctan2(arr8, arr7) * 180 / pi
    winddir = np.mod(winddir_over, 360)
    wd = winddir


    # print(u)
    # print(v)
    # print('this is winddir')
    # print(winddir)
    # print('this is not winddir anymore')

    # concentrations_________________________________________________________________________________________-

    # Open pollution file with aircraft pollution
    dataDIR = '../data/Aerosol.24h.JUL.ON.nc4'
    DS = xr.open_dataset(dataDIR)

    #print(DS.var)

    # Get data set with right location and times from file
    # da=DS.PM25.sel(lat=y, lon=x, method='nearest')
    # da = da.sel(time=slice('2005-07-20T00:30:00.000000000', '2005-07-22T23:30:00.000000000'))
    da1 = DS.PM25.sel(lat=y, lon=x, lev=1,method='nearest')
    #da1 = da1.sel(time=slice('2005-07-20T00:30:00.000000000', '2005-07-22T23:30:00.000000000'))

    # Make array with average of 3 hours to match wind data

    # _______________________________________________________________________

    # Open pollution file without aircraft pollution
    dataDIR = '../data/Aerosol.24h.JUL.OFF.nc4'
    DS = xr.open_dataset(dataDIR)

    # Make datasets for all locations around middle point
    da2 = DS.PM25.sel(lat=y, lon=x, lev=1,method='nearest')
    #da2 = da2.sel(time=slice('2005-07-20T00:30:00.000000000', '2005-07-22T23:30:00.000000000'))


    # Make array with average of 3 hours to match wind data, while choosing correct dataset to match wind direction


    # Substract pollution on and off to come to aircraft pollution
    ws = da1 - da2

    # plotting__________________________________________________________________________________________________
    # Set location of subplots around middle point
    if k == 0:
        plotloc = 1
        print('óne')
        print(wd)
        print('two')
        print(ws)
        print('three')
    elif k == 1:
        plotloc = 2
    elif k == 2:
        plotloc = 3
    elif k == 3:
        plotloc = 6
    elif k == 4:
        plotloc = 9
    elif k == 5:
        plotloc = 8
    elif k == 6:
        plotloc = 7
    elif k == 7:
        plotloc = 4



    # Make wind rose plot
    ax = fig.add_subplot(3, 3, plotloc, projection='windrose')
    ax.bar(wd, ws, nsector=8, bins=np.arange(0, 0.028, 0.004), cmap=cm.OrRd, opening=0.85, edgecolor='white')

    # Make wind rose plot
    #ax = WindroseAxes.from_ax()
    #ax.bar(wd, ws, nsector=8, bins=np.arange(0, 0.028, 0.004), cmap=cm.OrRd, opening=0.8, edgecolor='white')
    # ax.set_legend()

plt.show()