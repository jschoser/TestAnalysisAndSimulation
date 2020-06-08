# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 08:55:17 2020

@author: Egon Beyne
"""

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from Altitude_converter import eta_to_altitude_arr
from Country_reader import Europe_Coordinates, Country_Coordinates

# File to be analysed
filename    = "Data/Aerosol.24h.JUL.OFF.nc4"
filename_on = "Data/Aerosol.24h.JUL.ON.nc4"

# Extract dataset from file
DS = xr.open_dataset(filename)
DS_ON = xr.open_dataset(filename_on)

# Isolate aviation pollution
DS = DS_ON - DS

# Select pollutant
da = DS.PM25#DS.SpeciesConc_O3*1e9#DS.AerMassBC

# ========================================= Sample locations =================================================

lat = da.lat.values
lon = da.lon.values

# List to append coordinates to
coords = []

# Append all latitude and longitude coordinates to a list
for i in lon:
    for j in lat:
        coords.append([i, j])

# All coordinates of the dataset
coords = np.array(coords)

# Coordinates of land only
Europe = Europe_Coordinates()

# Remove the duplicate elements from coords and Europe, to select the sea only
Sea = np.array(list(set(map(tuple, coords)) - set(map(tuple, Europe))))

# Get the grid points in germany
Germany = Country_Coordinates('Germany')

# Locations to sample vertical distributions
sample_locations = [np.array([[20, 40]]),  # , 'Frankfurt Airport'],
                    0,  # Ocean
                    0,  # Germany
                    0]

location_names = ["Frankfurt Airport",
                  "Ocean",
                  "Germany",
                  "Continental Europe"]

# Add the datapoints in the sea to the sample locations
sample_locations[1] = Sea

# Add the datapoints in germany
sample_locations[2] = Germany

# Add the datapoints of continental Europe
sample_locations[3] = Europe

# Maximum altitude level to make the plots for
max_level = 38


def average_distributions(dataset, locations):
    """
    This function makes average pollution distributions for a given set of samples.
    As an input groups of different datasets for different areas can be given,
    The function will return an average distribution for every area.


    Parameters
    ----------
    dataset : Dataset containing all positions and altitudes, but averaged over time
    locations : List containing arrays with sample groups to be averaged

    Returns
    -------
    samples_averaged : Array containing the averaged vertical distribution for every sample group

    """

    # Make an empty array to store the data for each sample group
    samples_averaged = np.zeros((72, len(locations)))

    # Iterate through the different sample groups
    for i, sample in enumerate(locations):

        data_summed = 0

        # Sum the pollution for every sample in a sample group
        for j, datapoint in enumerate(sample):
            data_summed += dataset.sel(lat=datapoint[1], method='nearest').sel(lon=datapoint[0], method='nearest')

        # Divide by the length of the sample group to obtain the average
        sample_avg = np.array(data_summed) / len(sample)

        # Store the averaged sample data
        samples_averaged[:, i] = sample_avg

    return samples_averaged


avg_dat = 0

# Iterate through each time step to sum all pollution
for time in range(da.time.size):
    da_1 = da.sel(time=da.time.values[time])
    avg_dat += da_1

# Divide sum of all pollution by number of time steps tp get an average
avg_dat = avg_dat / da.time.size

# Get the averaged samples
samples_averaged = average_distributions(avg_dat, sample_locations)

# Convert the eta pressure levels to km, used as y axis in the plot
alt = eta_to_altitude_arr(da.lev.values)[:max_level]

# Plotting the different locations
for i in range(len(sample_locations)):
    plt.plot(samples_averaged[:max_level, i], alt, label=location_names[i])

plt.ylabel('Altitude [km]')
plt.xlabel('PM$_{2.5}$ concentration [$μg/m^3$]')#'Ozone mixing ratio [ppbv]')

plt.xlim(-.02,.12)
plt.ylim(0,18)

plt.legend()
plt.grid()
plt.show()

