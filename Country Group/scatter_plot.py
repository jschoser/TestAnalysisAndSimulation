import country_tools as ct
import numpy as np
from matplotlib import pyplot as plt
from collections import OrderedDict
import pandas
import seaborn as sb

"""
Scatter plot of all countries in the region, with emission and pollution axes

@author Jakob Schoser
"""
British_Isles = ["British Isles", "Ireland", "United Kingdom"]
Asian= ["Asian", "Iraq", "Iran", "Palestine","Israel","Lebanon","Jordan","Syria","Saudi Arabia"]
Iberian_Peninsula = ["Iberian Peninsula", "Spain", "Portugal"]
Southeast = ["Southeast","Greece","North Macedonia", "Albania", "Bulgaria", "Bosnia and Herzegovina","Serbia","Montenegro"]
Scandinavia = ["Nordic Countries", "Sweden", "Norway", "Denmark", "Finland"]
Central_Europe = ["Central Europe", "Hungary", "Croatia", "Slovenia", "Slovakia", "Austria", "Czechia"]
Turkey = ["Turkey etc", "Turkey", "Armenia", "Georgia", "Azerbaijan", "Cyprus"]
Baltics = ["Baltics", "Estonia", "Latvia", "Lithuania"]
Eastern_Europe = ["Eastern Europe","Russian Federation","Ukraine","Belarus","Kazakhstan","Moldova","Romania"]
Iceland = ["Icelandics", "Iceland", "Faroes"]
# Romania = ["Romania","Romania"]
# Finland = ["Finland","Finland"]
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
# Egypt = ["Egypt","Egypt"]
All_groups = [British_Isles, Asian, Iberian_Peninsula, Southeast, Scandinavia, Central_Europe, Turkey,Baltics ,Eastern_Europe ,Iceland ,Germany ,France ,Switzerland ,Italy ,Poland ,Belgium ,Netherlands ,Luxembourg ,Morocco ,Algeria , Tunisia ]

summer = False   # used to select between pollution data for January and July

poll_coll = "Aerosol.24h"  # the collection name for pollution (first part of the .nc4 filename)

# the chemicals to be taken into account for pollution and emissions, respectively. These need to be the names of the
# data sets inside the .nc4 files you selected
poll_chemical = "AerMassSO4"
em_chemical = "BC"

em_mult = 1
poll_mult = 1

# the altitude levels over which emissions will be considered (available from 1 to 32). Check Altitude_levels.txt for
# conversion to km. Level 8: 1 km altitude, level 32: 13 km altitude
emission_levels = slice(0, 32)

method = ct.METHOD_AVG  # the way that the data is combined inside one country (median or area-weighted average)

print("Creating country polygons...")
countries = ct.create_country_polygons()

print("Retrieving raw pollution and emission data...")
data, _ = ct.find_poll_em_data(countries, poll_coll, em_chemical, poll_chemical, emission_levels, summer, mode=ct.RETURN_BOTH, method=method)

# The countries are grouped at the top of this code. Here we  loop through the groups and we then extract the areas,
# summarize them, multiply them with the emissions, and then# they are divided by the total area of a group (to
# normalize)
print("Grouping countries...")
ed,pd = [],[]
for group in All_groups:
    total_e, total_p, t_e, t_p, area = ([] for i in range(5))
    c_in_group = group[1::]
    for country in c_in_group:
        c_area = countries[country][1]
        total_e.append(data[country][0] * c_area)
        total_p.append(data[country][1] * c_area)
        area.append(c_area)
    t_e.append(group[0])
    t_p.append(group[0])
    final_e = sum(total_e)/sum(area)
    final_p = sum(total_p)/sum(area)
    t_e.append(final_e)
    t_p.append(final_p)
    ed.append(tuple(t_e))
    pd.append(tuple(t_p))
em_data = OrderedDict(ed)
poll_data = OrderedDict(pd)

print("Plotting...")
# Set fontsize with this parameter
# fontsize = 15

em_values = np.array(list(em_data.values()))
poll_values = np.array(list(poll_data.values()))
# Use the line below for scaling the map to fit everything in
plt.axis([min(em_values)*0.9, max(em_values)*11, min(poll_values)*0.9, max(poll_values)/0.8])

plt.scatter(em_values, poll_values, cmap='hsv', c=np.random.rand(len(em_values)))

# This list is where you can put the name of the countries
Scatter_country_List = ["Icelandics","Belgium","Netherlands","Luxembourg","Algeria","Morocco"]
for country in Scatter_country_List:
# for country in em_data:
    plt.annotate(country, [em_data[country], poll_data[country]]).set_fontsize(12) #,[em_data[country], poll_data[country]])

# plt.title(ct.generate_sub_title(poll_chemical, em_chemical, summer, emission_levels, method)).set_fontsize(5)
plt.xlabel(em_chemical + " Emission Mass from Aviation $[kg/m^2/day]$").set_fontsize(12)
plt.ylabel(("Average Ground-Level {} from Aviation " + ("$[\mu g/m^3]$"  # not quite sure about the pollution units
            if poll_chemical != "SpeciesConc_O3" else "$[mol/(mol of dry air)]$")).format(poll_chemical)).set_fontsize(8.5)
plt.yscale('log') # With this line you can change the type of graph
plt.xscale('log') # Double Logaritmic is the clearest
# print("Finished")
plt.show()

# print("Calculating Correlation")
# # Calculate and plot the correlation between datasets
# dataset_cr = pandas.DataFrame({'emissions': em_values, 'pollution': poll_values}, columns=['emissions', 'pollution'])
# corr_type = 'pearson' # for a different correlation indicator, try method='spearman' or method='kendall'
# corr_data = dataset_cr.corr(method=corr_type)
#
# sb.heatmap(corr_data,
#             xticklabels=corr_data.columns,
#             yticklabels=corr_data.columns,
#             cmap='RdBu_r',
#             annot=True,
#             linewidth=0.5) # this plots the correlation
#                            # a coefficient close to 1 means that there is a positive correlation between the variables
#                            # the diagonal is equal to one as this is the correlation the variables to themselves
# print("Finished")
# plt.show()