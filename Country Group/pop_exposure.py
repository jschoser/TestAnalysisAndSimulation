import country_tools as ct
import xarray as xr
import operator
from pprint import PrettyPrinter
from matplotlib import pyplot as plt

"""
Used to calculate population exposure in total and per country

@author Jakob Schoser
"""

poll_coll = "O3.24h"  # the collection name for pollution (first part of the .nc4 filename)

# the chemicals to be taken into account for pollution and emissions, respectively. These need to be the names of the
# data sets inside the .nc4 files you selected
poll_chemical = "SpeciesConc_O3"

M_o3 = 47.99820
rho_air = 1.225
M_air = 28.97
o3_fac = M_o3 / M_air * rho_air * 1E6

poll_av_on_summer_filepath = ct.data_dir() / ct.data_filename(poll_coll, True, True)
poll_av_off_summer_filepath = ct.data_dir() / ct.data_filename(poll_coll, True, False)
poll_av_on_winter_filepath = ct.data_dir() / ct.data_filename(poll_coll, False, True)
poll_av_off_winter_filepath = ct.data_dir() / ct.data_filename(poll_coll, False, False)
pop_filepath = ct.data_dir() / "Population.nc4"

poll_av_on_summer_DS = xr.open_dataset(poll_av_on_summer_filepath)
poll_av_off_summer_DS = xr.open_dataset(poll_av_off_summer_filepath)
poll_av_on_winter_DS = xr.open_dataset(poll_av_on_winter_filepath)
poll_av_off_winter_DS = xr.open_dataset(poll_av_off_winter_filepath)
pop_DS = xr.open_dataset(pop_filepath)

poll_summer_da = getattr(poll_av_on_summer_DS, poll_chemical) - getattr(poll_av_off_summer_DS, poll_chemical)
poll_winter_da = getattr(poll_av_on_winter_DS, poll_chemical) - getattr(poll_av_off_winter_DS, poll_chemical)
pop_da = pop_DS.pop

poll_summer_da = poll_summer_da.sel(lev=1, method='nearest').sum(dim='time') / 21
poll_winter_da = poll_winter_da.sel(lev=1, method='nearest').sum(dim='time') / 21
poll_da = (poll_summer_da + poll_winter_da) / 2

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

# print("############################################################\n")

tot = pop_poll_da.sum().values

polygons = ct.create_country_polygons()
poll_per_country_summer, _ = ct.find_poll_em_data(polygons, poll_coll, "NO2", poll_chemical, slice(0, 32), True,
                                        mode=ct.RETURN_POLLUTION, method=ct.METHOD_POP)

poll_per_country_winter, _ = ct.find_poll_em_data(polygons, poll_coll, "NO2", poll_chemical, slice(0, 32), False,
                                        mode=ct.RETURN_POLLUTION, method=ct.METHOD_POP)

poll_values = [(s + w) / 2 for s, w in zip(poll_per_country_summer.values(), poll_per_country_winter.values())]
poll_per_country = {k: v / tot * 100 for k, v in zip(poll_per_country_summer.keys(), poll_values)}

pp = PrettyPrinter(indent=4)
pp.pprint(sorted(poll_per_country.items(), key=lambda item: item[1]))

# print(sum(poll_per_country.values())) # For some reason this is different


print("Sum:", tot * (o3_fac if "O3" in poll_chemical else 1))

plt.show()
