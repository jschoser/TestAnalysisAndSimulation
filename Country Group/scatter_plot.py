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
All_groups = [British_Isles, Asian, Iberian_Peninsula, Southeast, Scandinavia, Central_Europe, Turkey,Baltics ,Eastern_Europe ,Iceland ,Germany ,France ,Switzerland ,Italy ,Poland ,Belgium ,Netherlands ,Luxembourg ,Morocco ,Algeria , Tunisia]

summer = True   # used to select between pollution data for January and July

poll_coll = "O3.24h"  # the collection name for pollution (first part of the .nc4 filename)

# the chemicals to be taken into account for pollution and emissions, respectively. These need to be the names of the
# data sets inside the .nc4 files you selected
poll_chemical = "SpeciesConc_O3"
em_chemical = "NO2"

em_mult = 1
poll_mult = 1

# the altitude levels over which emissions will be considered (available from 1 to 32). Check Altitude_levels.txt for
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

ed = []
for group in All_groups:
    total = []
    c_in_group = group[1::]
    t = []
    area = []
    for country in c_in_group:
        c_area = countries[country][1]
        total.append(em_data[country]*c_area)
        area.append(c_area)
    t.append(group[0])
    final = (sum(total)/(sum(area)))
    t.append(final)
    t = tuple(t)
    ed.append(t)
ed = OrderedDict(ed)

em_data = ed

pd = []
for group in All_groups:
    total = []
    c_in_group = group[1::]
    t = []
    area = []
    for country in c_in_group:
        c_area = countries[country][1]
        total.append(poll_data[country] * c_area)
        area.append(c_area)
    t.append(group[0])
    final = (sum(total) / (sum(area)))
    t.append(final)
    t = tuple(t)
    pd.append(t)
pd = OrderedDict(pd)

poll_data = pd

print("Plotting...")
em_values = np.array(list(em_data.values()))
poll_values = np.array(list(poll_data.values()))

plt.axis([min(em_values), max(em_values), min(poll_values), max(poll_values)])

plt.scatter(em_values, poll_values, cmap='hsv', c=np.random.rand(len(em_values)))

for country in em_data:
    plt.annotate(country, [em_data[country], poll_data[country]])

plt.title(ct.generate_sub_title(poll_chemical, em_chemical, summer, emission_levels, method))
plt.xlabel(em_chemical + " Emission Mass from Aviation $[kg/day/km^2]$")
plt.ylabel(("Average Ground-Level {} from Aviation " + "$[\mu g/m/km^2]$"  # not quite sure about the pollution units
            if poll_chemical != "SpeciesConc_O3" else "$[mol/(mol of dry air)/km^2]$").format(poll_chemical))
plt.yscale('log') #With this line you can change the type of graph
plt.xscale('log') # Double Logaritmic is the clearest
print("Finished")
plt.show()

# Calculate and plot the correlation between datasets
dataset_cr = pandas.DataFrame({'emissions': em_values, 'pollution': poll_values}, columns=['emissions', 'pollution'])
corr_type = 'pearson' # for a different correlation indicator, try method='spearman' or method='kendall'
corr_data = dataset_cr.corr(method=corr_type)

sb.heatmap(corr_data,
            xticklabels=corr_data.columns,
            yticklabels=corr_data.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5) # this plots the correlation
                           # a coefficient close to 1 means that there is a positive correlation between the variables
                           # the diagonal is equal to one as this is the correlation the variables to themselves

plt.show()
