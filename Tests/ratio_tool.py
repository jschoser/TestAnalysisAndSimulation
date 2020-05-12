import numpy as np
from pprint import PrettyPrinter
import matplotlib.pyplot as plt
import statistics as stats

# =============================================================================
# --------------------AIRCRAFT ONLY DATA---------------------------------------
# =============================================================================

air_only = np.array([   ('Albania', 0.016983942252075473),
                        ('Algeria', 0.01131720344217956),
                        ('Armenia', 0.011897911658582314),
                        ('Austria', 0.04614698459652412),
                        ('Azerbaijan', 0.007169303085120826),
                        ('Belarus', 0.017911954628715893),
                        ('Belgium', 0.06118201856957153),
                        ('Bosnia and Herzegovina', 0.02253928341419941),
                        ('Bulgaria', 0.017643339531504987),
                        ('Croatia', 0.022764045956120083),
                        ('Cyprus', 0.01494664994497148),
                        ('Czechia', 0.03950648480762806),
                        ('Denmark', 0.018840597183654814),
                        ('Egypt', 0.015099162147158668),
                        ('Estonia', 0.006444946138157657),
                        ('Faroes', 0.0007712657988211191),
                        ('Finland', 0.004504321284364849),
                        ('France', 0.023462016227253912),
                        ('Georgia', 0.012329857708175993),
                        ('Germany', 0.04498971365089891),
                        ('Greece', 0.013020614830797814),
                        ('Hungary', 0.02896243913021693),
                        ('Iceland', 0.0007494442663665745),
                        ('Iran', 0.011524566499320075),
                        ('Iraq', 0.013002922178918927),
                        ('Ireland', 0.018018753944536246),
                        ('Israel', 0.022236412529584776),
                        ('Italy', 0.028418823614659403),
                        ('Jordan', 0.015832381972544104),
                        ('Kazakhstan', 0.006228152567788367),
                        ('Latvia', 0.01083218832008448),
                        ('Lebanon', 0.022954587754992067),
                        ('Libya', 0.013009893378826569),
                        ('Lithuania', 0.0169400628281445),
                        ('Luxembourg', 0.04794120788574219),
                        ('Moldova', 0.017666201656888026),
                        ('Montenegro', 0.016573120355673137),
                        ('Morocco', 0.00658717717195607),
                        ('Netherlands', 0.050802686513159424),
                        ('North Macedonia', 0.014824482726663908),
                        ('Norway', 0.0028333995241439703),
                        ('Palestine', 0.0184506257966389),
                        ('Poland', 0.024082320380873955),
                        ('Portugal', 0.00592583891219008),
                        ('Romania', 0.02460929195622396),
                        ('Russian Federation', 0.009579638002147397),
                        ('Saudi Arabia', 0.01273163754571137),
                        ('Serbia', 0.01697693253415587),
                        ('Slovakia', 0.030466785108720546),
                        ('Slovenia', 0.03369978616660528),
                        ('Spain', 0.009664108552136551),
                        ('Sweden', 0.006086644020898871),
                        ('Switzerland', 0.05094398339299193),
                        ('Syria', 0.016041674949130093),
                        ('Tunisia', 0.012603050864594487),
                        ('Turkey', 0.016101938949025594),
                        ('Ukraine', 0.015756099875665612),
                        ('United Kingdom', 0.0131140020855781)])

# =============================================================================
# --------------------BASE (AIRCRAFT OFF) DATA---------------------------------
# =============================================================================

air_off = np.array([    ('Albania', 11.008944668602071),
                        ('Algeria', 14.930076929727152),
                        ('Armenia', 14.740608803667834),
                        ('Austria', 13.177808006478951),
                        ('Azerbaijan', 13.32066347202923),
                        ('Belarus', 10.015280409696775),
                        ('Belgium', 16.68678694911664),
                        ('Bosnia and Herzegovina', 12.678053735542365),
                        ('Bulgaria', 14.462254645967326),
                        ('Croatia', 12.562519210492757),
                        ('Cyprus', 11.902864244249132),
                        ('Czechia', 12.279647445926866),
                        ('Denmark', 11.336396399155072),
                        ('Egypt', 11.605025336855935),
                        ('Estonia', 4.8865488450195045),
                        ('Faroes', 2.9083940729044544),
                        ('Finland', 3.6048977839139313),
                        ('France', 8.839960348355381),
                        ('Georgia', 12.419476449485575),
                        ('Germany', 13.772541954422007),
                        ('Greece', 12.602572485575083),
                        ('Hungary', 12.990101649960277),
                        ('Iceland', 2.2788192383448966),
                        ('Iran', 13.55300071585676),
                        ('Iraq', 18.284062011908595),
                        ('Ireland', 6.6323885118407215),
                        ('Israel', 17.21457181474575),
                        ('Italy', 11.104273862607842),
                        ('Jordan', 15.04423410718172),
                        ('Kazakhstan', 7.1351550089912985),
                        ('Latvia', 7.010328709070831),
                        ('Lebanon', 14.90570084689268),
                        ('Libya', 11.581302448175517),
                        ('Lithuania', 9.220544362599336),
                        ('Luxembourg', 12.760970342726935),
                        ('Moldova', 12.164789450810783),
                        ('Montenegro', 10.114563590017289),
                        ('Morocco', 10.696468913200567),
                        ('Netherlands', 15.943509748008942),
                        ('North Macedonia', 12.372539650494058),
                        ('Norway', 2.663965067777264),
                        ('Palestine', 20.49204278304136),
                        ('Poland', 11.392485377562268),
                        ('Portugal', 9.74195097694564),
                        ('Romania', 14.116451682046048),
                        ('Russian Federation', 7.772631847375137),
                        ('Saudi Arabia', 13.037347611822108),
                        ('Serbia', 13.706291125601055),
                        ('Slovakia', 13.12847449085983),
                        ('Slovenia', 14.69848927565308),
                        ('Spain', 7.354455637889519),
                        ('Sweden', 3.795035635174618),
                        ('Switzerland', 11.707395640985533),
                        ('Syria', 15.671058390553045),
                        ('Tunisia', 12.816494804332333),
                        ('Turkey', 11.877179809908142),
                        ('Ukraine', 11.131591976841891),
                        ('United Kingdom', 7.08611583824779)])

# SUMMER DIFFERENCE:

summer =    [   ('Albania', 11.008944668602071),
    #('Algeria', 14.930076929727152), africa
    #('Armenia', 14.740608803667834), asia
    ('Austria', 13.177808006478951),
    #('Azerbaijan', 13.32066347202923), asia
    ('Belarus', 10.015280409696775),
    #('Belgium', 16.68678694911664),
    ('Bosnia and Herzegovina', 12.678053735542365),
    ('Bulgaria', 14.462254645967326),
    ('Croatia', 12.562519210492757),
    ('Cyprus', 11.902864244249132),
    ('Czechia', 12.279647445926866),
    #('Denmark', 11.336396399155072),
    #('Egypt', 11.605025336855935), africa
    ('Estonia', 4.8865488450195045),
    #('Faroes', 2.9083940729044544),
    #('Finland', 3.6048977839139313),
    #('France', 8.839960348355381), western europe
    #('Georgia', 12.419476449485575), middle east
    ('Germany', 13.772541954422007),
    ('Greece', 12.602572485575083),
    #('Hungary', 12.990101649960277),
    #('Iceland', 2.2788192383448966),
    #('Iran', 13.55300071585676), middle east
    #('Iraq', 18.284062011908595), middle east
    #('Ireland', 6.6323885118407215),
    #('Israel', 17.21457181474575),
    #('Italy', 11.104273862607842),
    #('Jordan', 15.04423410718172),
    #('Kazakhstan', 7.1351550089912985),
    ('Latvia', 7.010328709070831),
    #('Lebanon', 14.90570084689268), middle east
    #('Libya', 11.581302448175517), africa
    ('Lithuania', 9.220544362599336),
    #('Luxembourg', 12.760970342726935), large error
    ('Moldova', 12.164789450810783),
    ('Montenegro', 10.114563590017289),
    #('Morocco', 10.696468913200567), africa
    #('Netherlands', 15.943509748008942),
    ('North Macedonia', 12.372539650494058),
    #('Norway', 2.663965067777264),
    #('Palestine', 20.49204278304136), large error
    ('Poland', 11.392485377562268),
    #('Portugal', 9.74195097694564), southern europe
    ('Romania', 14.116451682046048),
    ('Russian Federation', 7.772631847375137),
    #('Saudi Arabia', 13.037347611822108), middle east
    ('Serbia', 13.706291125601055),
    ('Slovakia', 13.12847449085983),
    ('Slovenia', 14.69848927565308),
    #('Spain', 7.354455637889519),
    #('Sweden', 3.795035635174618),
    ('Switzerland', 11.707395640985533),
    #('Syria', 15.671058390553045),
    #('Tunisia', 12.816494804332333), africa
    #('Turkey', 11.877179809908142), middle east
    ('Ukraine', 11.131591976841891),
    #('United Kingdom', 7.08611583824779)
    ]
summer = np.array(summer)

# WINTER DIFFERENCE:

winter = [   ('Albania', 18.550506668010833),
    #('Algeria', 7.695542349218552),
    #('Armenia', 17.684723389435824),
    ('Austria', 20.455824299421376),
    #('Azerbaijan', 20.688225627838957),
    ('Belarus', 24.9815413358632),
    #('Belgium', 28.372976581238955),
    ('Bosnia and Herzegovina', 23.328076687662588),
    ('Bulgaria', 24.841718575739904),
    ('Croatia', 24.405291981871837),
    ('Cyprus', 11.477403913225448),
    ('Czechia', 26.12465075180815),
    #('Denmark', 13.016131346939353),
    #('Egypt', 12.99962924775623),
    ('Estonia', 19.94596823553558),
    #('Faroes', 3.567276757400813),
    #('Finland', 14.254778759735661),
    #('France', 18.60233083269319),
    #('Georgia', 18.62420976806414),
    ('Germany', 24.574162176454685),
    ('Greece', 14.50629014870531),
    #('Hungary', 30.894349141681932),
    #('Iceland', 3.0680501070037485),
    #('Iran', 15.033270548242823),
    #('Iraq', 16.11264245521872),
    #('Ireland', 6.211406493770096),
    #('Israel', 14.881061271867726),
    #('Italy', 16.14226190316309),
    #('Jordan', 12.888194217850542),
    #('Kazakhstan', 13.087967451692725),
    ('Latvia', 22.001620557515437),
    #('Lebanon', 15.443608822409756),
    #('Libya', 10.26264483731209),
    ('Lithuania', 22.53747937573854),
    #('Luxembourg', 29.441737583705358),
    ('Moldova', 30.616103231180603),
    ('Montenegro', 16.577086467642413),
    #('Morocco', 8.384067488142868),
    #('Netherlands', 21.570651260350267),
    ('North Macedonia', 26.711767398941674),
    #('Norway', 4.5911571607848),
    #('Palestine', 15.781254674518602),
    ('Poland', 25.645194244206454),
    #('Portugal', 12.931799486933054),
    ('Romania', 30.605931954220612),
    ('Russian Federation', 18.151251655602536),
    #('Saudi Arabia', 11.924777733941763),
    ('Serbia', 30.352031314351454),
    ('Slovakia', 30.15309724863648),
    ('Slovenia', 26.625298682358753),
    #('Spain', 11.599115975550271),
    #('Sweden', 7.560629927910009),
    ('Switzerland', 17.91989550717018),
    #('Syria', 17.53650962726296),
    #('Tunisia', 10.198847787074614),
    #('Turkey', 20.952728089383566),
    ('Ukraine', 26.417495648154667),
    #('United Kingdom', 8.58195205640678)
    ]
winter = np.array(winter)

# =============================================================================

# Initialize arrays to store ratio and percentage
ratio_arr = []
perc_arr_named = []
perc_arr_val = []
tot = 0

# =============================================================================

# Calculate ratios and percentages
for i in range(len(winter)):
    if winter[i, 0] != summer[i, 0]:
        print('ERROR: ARRAY ELEMENTS (index = ' + str(i) +' ) NOT COHERENT')

    ratio = float(winter[i,1]) / float(summer[i,1])
    tot += ratio

    ratio_arr.append([winter[i, 0], ratio])
    perc_arr_named.append([winter[i, 0], round(ratio*100, 3)])
    perc_arr_val.append(ratio*100)

avg = tot / len(perc_arr_val) * 100
med = np.median(perc_arr_val)
stddev = stats.stdev(perc_arr_val)

# =============================================================================

# Print ratio array in a nice way
pp = PrettyPrinter(indent=4)
# pp.pprint(perc_arr_named)

# print('MEAN = ' + str(avg))
# print('MEDIAN = ' + str(med))
# print('SD = ' + str(stddev))

# ==============================================================================
split_low = []
split_upp = []
split_mid = []

named_low = []
named_mid = []
named_upp = []

data_mean = np.mean(perc_arr_val)
data_sd = stats.stdev(perc_arr_val)
sd_m = 2    #standard dev. multiplier

high_outliers = []
low_outliers = []

print('Outlier bounds: ' + str(round(data_mean - sd_m * data_sd,2)) + ', ' + str(round(data_mean + sd_m * data_sd,2)))

for i in range(len(perc_arr_val)):
    if perc_arr_val[i] < data_mean - sd_m * data_sd:
        split_low.append(perc_arr_val[i])
        named_low.append(perc_arr_named[i])

    elif data_mean - sd_m * data_sd <= perc_arr_val[i] <= data_mean + sd_m * data_sd:
        split_mid.append(perc_arr_val[i])
        named_mid.append(perc_arr_named[i])
    else:
        split_upp.append(perc_arr_val[i])
        named_upp.append(perc_arr_named[i])

# ========================================================================================

# Print outliers
print(named_low)
print(named_mid)
print(named_upp)

# =======================================================================================

# Stat data
main_mean = np.mean(perc_arr_val)
main_sd = stats.stdev(perc_arr_val)
main_median = stats.median(perc_arr_val)

print('TOTAL: MEAN = ' + str(round(main_mean,2)) + ' SD = ' + str(round(main_sd,2)) \
      + ' MEDIAN = ' + str(round(main_median,2)))

if len(split_low) > 2:
    low_mean = np.mean(split_low)
    low_sd = stats.stdev(split_low)
    print('LOW: MEAN = ' + str(round(low_mean,2)) + ' SD = ' + str(round(low_sd,2)))

mid_mean = np.mean(split_mid)
mid_sd = stats.stdev(split_mid)
print('MID: MEAN = ' + str(round(mid_mean,2)) + ' SD = ' + str(round(mid_sd,2)))

if len(split_upp) > 2:
    upp_mean = np.mean(split_upp)
    upp_sd = stats.stdev(split_upp)
    print('UPP: MEAN = ' + str(round(upp_mean,2)) + ' SD = ' + str(round(upp_sd)))

# =================================================================================

# Make boxplot

fig, axs = plt.subplots()

#data = [split_low, split_upp]
data = perc_arr_val

bp = axs.boxplot(data, vert=False, showmeans=True, meanline=True)

maxval = round(np.max(perc_arr_val))

major_ticks = np.arange(0, maxval, 50)
minor_ticks = np.arange(0, maxval, 10)
axs.set_xticks(major_ticks)
axs.set_xticks(minor_ticks, minor=True)

axs.grid(which='minor', alpha=0.2)
axs.grid(which='major', alpha=0.5)

axs.set_yticks([])

# plt.title('% Summer to winter aircraft-attributable PM2.5')

plt.tight_layout()
plt.show()