import json
import numpy as np
import matplotlib.pyplot as plt


def Europe_Coordinates():
    # Open the json file
    with open("country_cells.json", "r") as read_file:
        data = json.load(read_file)

    # Make a list containing the names of all the countries
    countries = list(data)

    Europe = []

    # Iterate through all the given countries
    for country in countries:
        # Get all the grid cells within a certain country
        coord = list(data[country])

        # Attach the country coordinates to the list containing all the coordinates of europe
        Europe.extend(list(coord))

    Europe = np.array(Europe)
    return Europe


def Country_Coordinates(country):
    # Open the json file
    with open("country_cells.json", "r") as read_file:
        data = json.load(read_file)

    # Select the grid points of one country
    coord = list(data[country])

    return np.array(coord)


