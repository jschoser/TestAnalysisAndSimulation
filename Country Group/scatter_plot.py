import country_tools as ct
import numpy as np
from matplotlib import pyplot as plt
from collections import OrderedDict

"""
Scatter plot of all countries in the region, with emission and pollution axes

@author Jakob Schoser
"""
British_Isles = ["British Isles", "Ireland", "United Kingdom"]
Asian= ["Asian", "Iraq", "Iran", "Palestine","Israel","Lebanon","Jordan","Syria","Saudi Arabia"]
Iberian_Peninsula = ["Iberian Peninsula", "Spain", "Portugal"]
Southeast = ["Southeast","Greece","North Macedonia", "Albania", "Bulgaria", "Bosnia and Herzegovina","Serbia","Montenegro"]
Scandinavia = ["Scandinavia", "Sweden", "Norway", "Denmark"]
Central_Europe = ["Central Europe", "Hungary", "Croatia", "Slovenia", "Slovakia", "Austria", "Czechia"]
Turkey = ["Turkey and the Neighbours", "Turkey", "Armenia", "Georgia", "Azerbaijan", "Cyprus"]
Baltics = ["Baltics", "Estonia", "Latvia", "Lithuania"]
Eastern_Europe = ["Eastern Europe","Russian Federation","Ukraine","Belarus","Kazakhstan","Moldova"]
Iceland = ["Icelandics", "Iceland", "Faroes"]
Romania = ["Romania","Romania"]
Finland = ["Finland","Finland"]
Germany = ["Germany","Germany"]
France = ["France","France"]
Switzerland = ["Switzerland","Switzerland"]
Italy = ["Italy", "Italy"]
Poland = ["Poland","Poland"]
Belgium = ["Belgium", "Belgium"]
Netherlands = ["Netherlands", "Netherlands"]
Luxembourg = ["Luxembourg","Luxembourg"]
Morocco = ["Morocco", "Morocco"]
Algeria = ["Algeria","Algeria"]
Libya = ["Libya", "Libya"]
Tunisia = ["Tunisia", "Tunisia"]
Egypt = ["Egypt","Egypt"]
All_groups = [British_Isles, Asian, Iberian_Peninsula, Southeast, Scandinavia, Central_Europe, Turkey,Baltics ,Eastern_Europe ,Iceland ,Romania ,Finland ,Germany ,France ,Switzerland ,Italy ,Poland ,Belgium ,Netherlands ,Luxembourg ,Morocco ,Algeria , Tunisia , Egypt ]

summer = True   # used to select between pollution data for January and July

poll_coll = "Soot.24h"  # the collection name for pollution (first part of the .nc4 filename)

# the chemicals to be taken into account for pollution and emissions, respectively. These need to be the names of the
# data sets inside the .nc4 files you selected
poll_chemical = "AerMassBC"
em_chemical = "BC"

em_mult = 1
poll_mult = 1

# the altitude levels over which emissions will be considered (available from 0 to 32). Check Altitude_levels.txt for
# conversion to km. Level 8: 1 km altitude, level 32: 13 km altitude
emission_levels = slice(0, 8)

method = ct.METHOD_AVG  # the way that the data is combined inside one country (median or area-weighted average)

print("Creating country polygons...")
countries = ct.create_country_polygons()

print("Retrieving raw pollution and emission data...")
raw_data, _ = ct.find_poll_em_data(countries, poll_coll, em_chemical, poll_chemical,
                                   emission_levels, summer)

print("Processing the data...")
em_data, _ = ct.process_data(countries, raw_data, method=method, mode=ct.PLOT_EMISSIONS, multiplier=em_mult)
poll_data, _ = ct.process_data(countries, raw_data, method=method, mode=ct.PLOT_POLLUTION, multiplier=poll_mult)

d = []
for group in All_groups:
    total = []
    countries = group[1::]
    t = []
    for country in countries:
        total.append(em_data[country])
    t.append(group.pop(0))
    t.append(sum(total))
    t = tuple(t)
    d.append(t)
d = OrderedDict(d)

em_data = d

d = []
for group in All_groups:
    total = []
    countries = group[1::]
    t = []
    for country in countries:
        total.append(poll_data[country])
    t.append(group.pop(0))
    t.append(sum(total))
    t = tuple(t)
    d.append(t)
d = OrderedDict(d)

poll_data = d

print("Plotting...")
em_values = np.array(list(em_data.values()))
poll_values = np.array(list(poll_data.values()))

plt.axis([min(em_values), max(em_values), min(poll_values), max(poll_values)])

plt.scatter(em_values, poll_values, cmap='hsv', c=np.random.rand(len(em_values)))

# for country in em_data:
#     plt.annotate(country, [em_data[country], poll_data[country]])

plt.title(ct.generate_sub_title(poll_chemical, em_chemical, summer, emission_levels, method))
plt.xlabel(em_chemical + " Emission Mass from Aviation $[kg/day/km^2]$")
plt.ylabel(("Average Ground-Level {} from Aviation " + "$[\mu g/m/km^2]$"
            if poll_chemical != "SpeciesConc_O3" else "$[mol/(mol of dry air)/km^2]$").format(poll_chemical))
plt.yscale('linear') #With this line you can change the type of graph
print("Finished")
plt.show()


# em_data = dict([('Albania', 1.2887232830806852e-19), ('Algeria', 9.615877358485282e-21)])
# poll_data = dict([('Albania', 3.962841252382609e-08), ('Algeria', 2.2985724546747333e-08)])

# d = []
# for group in All_groups:
#     total = []
#     countries = group[1::]
#     t = []
#     for country in countries:
#         total.append(em_data[country])
#     t.append(group.pop(0))
#     t.append(sum(total))
#     t = tuple(t)
#     d.append(t)
# d = OrderedDict(d)
#
# em_data = d
#
# print(d)
# # d[group.pop(0)] = sum(total)
# print(em_data)
