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

s_diff =    [   ('Albania', 0.016983942252075473),
    ('Algeria', 0.01131720344217956),
    ('Armenia', 0.011897911658582314),
    ('Austria', 0.04614698459652412),
    ('Azerbaijan', 0.007169303085120826),
    ('Belarus', 0.017911954628715893),
    ('Belgium', 0.06118201856957153),
    ('Bosnia and Herzegovina', 0.02253928341419941),
    ('Bulgaria', 0.017643339531504987),
    ('Croatia', 0.022764045956120083),
    #('Cyprus', 0.01494664994497148),
    ('Czechia', 0.03950648480762806),
    ('Denmark', 0.018840597183654814),
    #('Egypt', 0.015099162147158668),
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
    #('Ireland', 0.018018753944536246),
    ('Israel', 0.022236412529584776),
    ('Italy', 0.028418823614659403),
    #('Jordan', 0.015832381972544104),
    ('Kazakhstan', 0.006228152567788367),
    ('Latvia', 0.01083218832008448),
    ('Lebanon', 0.022954587754992067),
    #('Libya', 0.013009893378826569),
    ('Lithuania', 0.0169400628281445),
    ('Luxembourg', 0.04794120788574219),
    ('Moldova', 0.017666201656888026),
    ('Montenegro', 0.016573120355673137),
    ('Morocco', 0.00658717717195607),
    ('Netherlands', 0.050802686513159424),
    ('North Macedonia', 0.014824482726663908),
    ('Norway', 0.0028333995241439703),
    #('Palestine', 0.0184506257966389),
    ('Poland', 0.024082320380873955),
    ('Portugal', 0.00592583891219008),
    ('Romania', 0.02460929195622396),
    ('Russian Federation', 0.009579638002147397),
    #('Saudi Arabia', 0.01273163754571137),
    ('Serbia', 0.01697693253415587),
    ('Slovakia', 0.030466785108720546),
    ('Slovenia', 0.03369978616660528),
    ('Spain', 0.009664108552136551),
    ('Sweden', 0.006086644020898871),
    ('Switzerland', 0.05094398339299193),
    ('Syria', 0.016041674949130093),
    #('Tunisia', 0.012603050864594487),
    ('Turkey', 0.016101938949025594),
    ('Ukraine', 0.015756099875665612),
    ('United Kingdom', 0.0131140020855781)]
s_diff = np.array(s_diff)

# WINTER DIFFERENCE:

w_diff = [   ('Albania', 0.029744859137458498),
    ('Algeria', 0.008863826641201123),
    ('Armenia', 0.035123795832261606),
    ('Austria', 0.08022019454575562),
    ('Azerbaijan', 0.03208444000454896),
    ('Belarus', 0.03761542823864437),
    ('Belgium', 0.07657769246820342),
    ('Bosnia and Herzegovina', 0.03464149869918198),
    ('Bulgaria', 0.02278757643565538),
    ('Croatia', 0.0643934698926948),
    #('Cyprus', 0.008554231552850632),
    ('Czechia', 0.0766477368756012),
    ('Denmark', 0.04831800900431944),
    #('Egypt', 0.006359758831205823),
    ('Estonia', 0.019070436670845976),
    ('Faroes', 0.0011347487165140064),
    ('Finland', 0.01301060172221948),
    ('France', 0.06592947353525694),
    ('Georgia', 0.02998711900840723),
    ('Germany', 0.0903189655082281),
    ('Greece', 0.01610725931525713),
    ('Hungary', 0.0739080771348828),
    ('Iceland', 0.0008704911372366744),
    ('Iran', 0.029313415350927696),
    ('Iraq', 0.012861499789041218),
    #('Ireland', 0.008366256694747741),
    ('Israel', 0.015961076668531266),
    ('Italy', 0.06783644657053384),
    #('Jordan', 0.00915364057526803),
    ('Kazakhstan', 0.009988338893356659),
    ('Latvia', 0.025563785043323226),
    ('Lebanon', 0.024242223888014804),
    #('Libya', 0.004498385669318381),
    ('Lithuania', 0.036156656018847114),
    ('Luxembourg', 0.08827699933733259),
    ('Moldova', 0.04057011426747039),
    ('Montenegro', 0.014497424613869882),
    ('Morocco', 0.01395924692014025),
    ('Netherlands', 0.06952839547264533),
    ('North Macedonia', 0.03859960257847538),
    ('Norway', 0.005605852998444943),
    #('Palestine', 0.010712397276272729),
    ('Poland', 0.05863606446298291),
    ('Portugal', 0.03586413967972179),
    ('Romania', 0.043443063612352145),
    ('Russian Federation', 0.018572837395256274),
    #('Saudi Arabia', 0.004704854090017228),
    ('Serbia', 0.03066131382194287),
    ('Slovakia', 0.06210604361588843),
    ('Slovenia', 0.10528170218127014),
    ('Spain', 0.03968266080460739),
    ('Sweden', 0.014314957465463669),
    ('Switzerland', 0.07801704200705196),
    ('Syria', 0.01585247121071788),
    #('Tunisia', 0.008212136788902645),
    ('Turkey', 0.028548454391349884),
    ('Ukraine', 0.03476316636145003),
    ('United Kingdom', 0.019651767304355323)]
w_diff = np.array(w_diff)

# =============================================================================

# Initialize arrays to store ratio and percentage
ratio_arr = []
perc_arr_named = []
perc_arr_val = []
tot = 0

# =============================================================================

# Calculate ratios and percentages
for i in range(len(s_diff)):
    if s_diff[i, 0] != w_diff[i, 0]:
        print('ERROR: ARRAY ELEMENTS (index = ' + str(i) +' ) NOT COHERENT')

    ratio = float(s_diff[i,1]) / float(w_diff[i,1])
    tot += ratio

    ratio_arr.append([s_diff[i, 0], ratio])
    perc_arr_named.append([s_diff[i, 0], round(ratio*100, 3)])
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

threshold = 80
for i in range(len(perc_arr_val)):
    if perc_arr_val[i] < threshold:
        split_low.append(perc_arr_val[i])
        named_low.append(perc_arr_named[i])
    elif threshold <= perc_arr_val[i] <= (200 - threshold):
        split_mid.append(perc_arr_val[i])
        named_mid.append(perc_arr_named[i])
    else:
        split_upp.append(perc_arr_val[i])
        named_upp.append(perc_arr_named[i])

# =============================================================================

# Make boxplot

fig, axs = plt.subplots()

#data = [split_low, split_upp]
data = perc_arr_val

bp = axs.boxplot(data, vert=False, showmeans=True, meanline=True)

major_ticks = np.arange(0, 300, 25)
minor_ticks = np.arange(0, 300, 5)
axs.set_xticks(major_ticks)
axs.set_xticks(minor_ticks, minor=True)

axs.grid(which='minor', alpha=0.2)
axs.grid(which='major', alpha=0.5)

axs.set_yticks([])

plt.title('% Summer to winter aircraft-attributable PM2.5')

plt.tight_layout()
plt.show()

# =============================================================================

# Stat data

main_mean = np.mean(perc_arr_val)
main_sd = stats.stdev(perc_arr_val)
main_median = stats.median(perc_arr_val)

print('MAIN: MEAN = ' + str(round(main_mean,2)) + ' SD = ' + str(round(main_sd)) + ' MEDIAN = ' + str(round(main_median)))

low_mean = np.mean(split_low)
low_sd = stats.stdev(split_low)

print('LOW: MEAN = ' + str(round(low_mean,2)) + ' SD = ' + str(round(low_sd)))

mid_mean = np.mean(split_mid)
mid_sd = stats.stdev(split_mid)

upp_mean = np.mean(split_upp)
upp_sd = stats.stdev(split_upp)

print('UPP: MEAN = ' + str(round(upp_mean,2)) + ' SD = ' + str(round(upp_sd)))

outliers = []
for i in range(len(perc_arr_val)):
    if perc_arr_val[i] > 150:
        outliers.append(perc_arr_named[i])

print(outliers)