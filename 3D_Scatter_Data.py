# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:13:39 2020

@author: Egon Beyne
"""

import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


# Convert eta levels to altitude
def eta_to_altitude_arr(eta_array):
    
    # data
    alt_dat = np.genfromtxt("Altitude_levels.txt", skip_header = 3,usecols = (1, 2))
    
    # Grid points
    grid = alt_dat[:, 0]
    
    # Function values at grid points
    func = alt_dat[:,1]
    return np.interp(eta_array, grid, func)


def datapoints():
    
    # Path to datafiles
    file_on     = "Data/Soot.24h.JAN.ON.nc4"
    file_off    = "Data/Soot.24h.JAN.OFF.nc4"
    
    # Open datafile and select set
    DS_ON   = xr.open_dataset(file_on).AerMassBC
    DS_OFF  = xr.open_dataset(file_off).AerMassBC
    
    # Filtering out non-aviation data
    da      = DS_ON - DS_OFF
    
    # Threshold
    thrs = float(da.mean())*15
    
    
    # Store indices of location where pollution exceeds threshold
    sel = np.argwhere(np.array(da)>thrs)
    
    
    # Convert indices to coordinates
    lev = np.take(da.lev.values,sel[:, 1])
    lat = np.take(da.lat.values,sel[:, 2])
    lon = np.take(da.lon.values,sel[:, 3])
    
    # Change array type to float
    sel = sel.astype('float64')
    
    # Add coordinates to array
    sel[:, 1] = eta_to_altitude_arr(lev)
    sel[:, 2] = lat
    sel[:, 3] = lon
    
    return sel

sel = datapoints()


lev = sel[:, 1]
lat = sel[:, 2]
lon = sel[:, 3]



# Make figure for test plot
fig = plt.figure()

# Create axes
ax = plt.axes(projection = '3d')

# Plot datapoints
ax.scatter3D(lat, lon, lev)

plt.show()