from windrose import WindroseAxes
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
from vector_mapping import *

dataset = netcdf_dataset('../Data/wind/' + month + '/MERRA2.2005' + month + day + '.A3dyn.05x0625.EU.nc4')

X, Y = unpack_posdata()
U, V = unpack_veldata(0)

# Create wind speed and direction variables

ws = np.random.random(200) * 6
wd = np.random.random(200) * 360

# Make wind rose plot
ax = WindroseAxes.from_ax()
ax.bar(wd, ws, nsector=8, normed=True, opening=0.8, edgecolor='white')
ax.set_legend()

plt.show()

print(ws)
