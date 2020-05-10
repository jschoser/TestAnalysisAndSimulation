import country_tools as ct
import xarray as xr
import operator
from pprint import PrettyPrinter
from matplotlib import pyplot as plt

"""
Used to calculate population exposure in total and per country

@author Jakob Schoser
"""

summer = False   # used to select between pollution data for January and July

poll_coll = "Aerosol.24h"  # the collection name for pollution (first part of the .nc4 filename)

# the chemicals to be taken into account for pollution and emissions, respectively. These need to be the names of the
# data sets inside the .nc4 files you selected
poll_chemical = "PM25"

poll_av_on_filepath = ct.data_dir() / ct.data_filename(poll_coll, summer, True)
poll_av_off_filepath = ct.data_dir() / ct.data_filename(poll_coll, summer, False)
pop_filepath = ct.data_dir() / "Population.nc4"

poll_av_on_DS = xr.open_dataset(poll_av_on_filepath)
poll_av_off_DS = xr.open_dataset(poll_av_off_filepath)
pop_DS = xr.open_dataset(pop_filepath)

poll_da = getattr(poll_av_on_DS, poll_chemical) - getattr(poll_av_off_DS, poll_chemical)
pop_da = pop_DS.pop

poll_da = poll_da.sel(lev=1, method='nearest').sum(dim='time') / 21

pop_poll_da = poll_da * pop_da

# the median and standard deviation may not be all that useful, since they will change depending on how much of the
# sea we include
# print("Results on high-resolution grid:")
# print("Mean:", pop_poll_da.mean().values)
# print("Median:", pop_poll_da.median().values)
# print("Standard deviation:", pop_poll_da.std().values)
# print("Maximum:", pop_poll_da.max().values)
# print("Minimum:", pop_poll_da.min().values,"\n")
# print("Sum:", pop_poll_da.sum().values)

print("############################################################\n")

polygons = ct.create_country_polygons()
poll_per_country, _ = ct.find_poll_em_data(polygons, poll_coll, "NO2", poll_chemical, slice(0, 32), summer,
                                        mode=ct.RETURN_POLLUTION, method=ct.METHOD_POP)

max_country = max(poll_per_country.items(), key=operator.itemgetter(1))[0]
min_country = min(poll_per_country.items(), key=operator.itemgetter(1))[0]

print("Country with maximum exposure:", max_country, "with", poll_per_country[max_country])
# print("Country with minimum exposure:", min_country, "with", poll_per_country[min_country])

pp = PrettyPrinter(indent=4)
pp.pprint(poll_per_country)

print("Sum:", pop_poll_da.sum().values)
print(sum(poll_per_country.values()))

plt.show()
