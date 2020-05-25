import xarray as xr
import country_tools as ct
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

summer = True

DS_aero_on = xr.open_dataset(ct.data_dir() / ct.data_filename("Aerosol.24h", summer, True))
DS_aero_off = xr.open_dataset(ct.data_dir() / ct.data_filename("Aerosol.24h", summer, False))
DS_soot_on = xr.open_dataset(ct.data_dir() / ct.data_filename("Soot.24h", summer, True))
DS_soot_off = xr.open_dataset(ct.data_dir() / ct.data_filename("Soot.24h", summer, False))

das = {}
das["PM25"] = DS_aero_on.PM25 - DS_aero_off.PM25
das["SO4"] = DS_aero_on.AerMassSO4 - DS_aero_off.AerMassSO4
das["NIT"] = DS_aero_on.AerMassNIT - DS_aero_off.AerMassNIT
das["NH4"] = DS_aero_on.AerMassNH4 - DS_aero_off.AerMassNH4
das["POA"] = DS_soot_on.AerMassPOA - DS_soot_off.AerMassPOA
das["BC"] = DS_soot_on.AerMassBC - DS_soot_off.AerMassBC

factors = {"PM25": 1, "SO4": 1.233, "NIT": 1.233, "NH4": 1.233, "POA": 1.049, "BC": 1}

for da in das:
    das[da] = das[da].sel(lev=1, method='nearest').sum(dim='time') / 21
    das[da] = das[da].where(das[da].lon > -28.75, drop=True)
    das[da] = das[da].where(das[da].lon < 48.75, drop=True)
    das[da] = das[da].where(das[da].lat > 31, drop=True)
    das[da] = das[da].where(das[da].lat < 69, drop=True)
    das[da] *= factors[da]

da_tot = das["SO4"] + das["NIT"] + das["NH4"] + das["POA"] + das["BC"]

plt_idx = 321
proj = ccrs.PlateCarree()  # select projection. Only seems to work with PlateCarree though

for da in das:
    das[da] /= da_tot
    # das[da] = das[da].where(xr.ufuncs.isfinite(das[da]), other=0)
    ax = plt.subplot(plt_idx, projection=proj)
    ax.coastlines(resolution='50m')  # draw coastlines with given resolution
    das[da].plot(vmin=-1.5, vmax=1.5, cmap='coolwarm')
    plt_idx += 1

plt.show()
