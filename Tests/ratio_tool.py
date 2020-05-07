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

# =============================================================================

# Initialize arrays to store ratio and percentage
ratio_arr = []
perc_arr_named = []
perc_arr_val = []
tot = 0

# =============================================================================

# Calculate ratios and percentages
for i in range(len(air_only)):
    if air_only[i, 0] != air_off[i, 0]:
        print('ERROR: ARRAY ELEMENTS (index = ' + str(i) +' ) NOT COHERENT')

    ratio = float(air_only[i,1]) / float(air_off[i,1])
    tot += ratio

    ratio_arr.append([air_off[i, 0], ratio])
    perc_arr_named.append([air_off[i, 0], round(ratio*100, 3)])
    perc_arr_val.append(ratio*100)

avg = tot / len(perc_arr_val) * 100
med = np.median(perc_arr_val)
stddev = stats.stdev(perc_arr_val)

# =============================================================================

# Print ratio array in a nice way
pp = PrettyPrinter(indent=4)
# pp.pprint(perc_arr_named)

print('MEAN = ' + str(avg))
print('MEDIAN = ' + str(med))
print('SD = ' + str(stddev))

# =============================================================================

# Make boxplot
fig = plt.figure(1, figsize=(10, 3))
ax = fig.add_subplot(111)
bp = ax.boxplot(perc_arr_val, vert=False, showmeans=True, meanline=True, notch=True)

major_ticks = np.arange(0, 0.5, 0.05)
minor_ticks = np.arange(0, 0.45, 0.01)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)

ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

ax.set_yticks([])

plt.title('% of aircraft-attributable PM2.5 to base PM2.5')

plt.tight_layout()
plt.show()

