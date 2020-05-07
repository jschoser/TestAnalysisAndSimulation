import country_tools as ct
from cartopy import crs
import xarray as xr
import numpy as np
from matplotlib import pyplot as plt

summer = True   # used to select between pollution data for January and July

poll_coll = "Soot.24h"  # the collection name for pollution (first part of the .nc4 filename)

# the chemicals to be taken into account for pollution and emissions, respectively. These need to be the names of the
# data sets inside the .nc4 files you selected
poll_chemical = "AerMassBC"
em_chemical = "BC"

# the altitude levels over which emissions will be considered (available from 0 to 32). Check Altitude_levels.txt for
# conversion to km. Level 8: 1 km altitude, level 32: 13 km altitude
emission_levels = slice(0, 32)

# TODO: Ratio doesn't work yet, because apparently the grid is not the same in emissions and pollution?
mode = ct.RETURN_RATIO # the statistic which is plotted (emissions, pollution or ratio between them)

colormap = "coolwarm"  # the color map used. Google "matplotlib color maps" to see the options

vmin, vmax = 0, None  # extremes of the colour legend. If set to None, they are automatically chosen

ct.plot_high_res_map(poll_coll, em_chemical, poll_chemical, emission_levels, summer, mode, colormap=colormap,
                     vmin=vmin, vmax=vmax)

plt.show()
