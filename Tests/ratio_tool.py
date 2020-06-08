import numpy as np
from pprint import PrettyPrinter
import matplotlib.pyplot as plt
import statistics as stats

# =============================================================================
# ---------------------------SUMMER BACKGROUND---------------------------------
# =============================================================================

summer_bg = [('Albania', 11.008944668602071),
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
             ('United Kingdom', 7.08611583824779)]
summer_bg = np.array(summer_bg)

# =============================================================================
# ---------------------------WINTER BACKGROUND---------------------------------
# =============================================================================

winter_bg = [('Albania', 18.550506668010833),
             ('Algeria', 7.695542349218552),
             ('Armenia', 17.684723389435824),
             ('Austria', 20.455824299421376),
             ('Azerbaijan', 20.688225627838957),
             ('Belarus', 24.9815413358632),
             ('Belgium', 28.372976581238955),
             ('Bosnia and Herzegovina', 23.328076687662588),
             ('Bulgaria', 24.841718575739904),
             ('Croatia', 24.405291981871837),
             ('Cyprus', 11.477403913225448),
             ('Czechia', 26.12465075180815),
             ('Denmark', 13.016131346939353),
             ('Egypt', 12.99962924775623),
             ('Estonia', 19.94596823553558),
             ('Faroes', 3.567276757400813),
             ('Finland', 14.254778759735661),
             ('France', 18.60233083269319),
             ('Georgia', 18.62420976806414),
             ('Germany', 24.574162176454685),
             ('Greece', 14.50629014870531),
             ('Hungary', 30.894349141681932),
             ('Iceland', 3.0680501070037485),
             ('Iran', 15.033270548242823),
             ('Iraq', 16.11264245521872),
             ('Ireland', 6.211406493770096),
             ('Israel', 14.881061271867726),
             ('Italy', 16.14226190316309),
             ('Jordan', 12.888194217850542),
             ('Kazakhstan', 13.087967451692725),
             ('Latvia', 22.001620557515437),
             ('Lebanon', 15.443608822409756),
             ('Libya', 10.26264483731209),
             ('Lithuania', 22.53747937573854),
             ('Luxembourg', 29.441737583705358),
             ('Moldova', 30.616103231180603),
             ('Montenegro', 16.577086467642413),
             ('Morocco', 8.384067488142868),
             ('Netherlands', 21.570651260350267),
             ('North Macedonia', 26.711767398941674),
             ('Norway', 4.5911571607848),
             ('Palestine', 15.781254674518602),
             ('Poland', 25.645194244206454),
             ('Portugal', 12.931799486933054),
             ('Romania', 30.605931954220612),
             ('Russian Federation', 18.151251655602536),
             ('Saudi Arabia', 11.924777733941763),
             ('Serbia', 30.352031314351454),
             ('Slovakia', 30.15309724863648),
             ('Slovenia', 26.625298682358753),
             ('Spain', 11.599115975550271),
             ('Sweden', 7.560629927910009),
             ('Switzerland', 17.91989550717018),
             ('Syria', 17.53650962726296),
             ('Tunisia', 10.198847787074614),
             ('Turkey', 20.952728089383566),
             ('Ukraine', 26.417495648154667),
             ('United Kingdom', 8.58195205640678)]
winter_bg = np.array(winter_bg)

# =============================================================================
# --------------------------------SUMMER A/C-----------------------------------
# =============================================================================

summer_ac = [('Albania', 0.016983942252075473),
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
             ('United Kingdom', 0.0131140020855781)]
summer_ac = np.array(summer_ac)

# =============================================================================
# --------------------------------WINTER A/C ----------------------------------
# =============================================================================

winter_ac = [('Albania', 0.029744859137458498),
             ('Algeria', 0.008863826641201123),
             ('Armenia', 0.035123795832261606),
             ('Austria', 0.08022019454575562),
             ('Azerbaijan', 0.03208444000454896),
             ('Belarus', 0.03761542823864437),
             ('Belgium', 0.07657769246820342),
             ('Bosnia and Herzegovina', 0.03464149869918198),
             ('Bulgaria', 0.02278757643565538),
             ('Croatia', 0.0643934698926948),
             ('Cyprus', 0.008554231552850632),
             ('Czechia', 0.0766477368756012),
             ('Denmark', 0.04831800900431944),
             ('Egypt', 0.006359758831205823),
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
             ('Ireland', 0.008366256694747741),
             ('Israel', 0.015961076668531266),
             ('Italy', 0.06783644657053384),
             ('Jordan', 0.00915364057526803),
             ('Kazakhstan', 0.009988338893356659),
             ('Latvia', 0.025563785043323226),
             ('Lebanon', 0.024242223888014804),
             ('Libya', 0.004498385669318381),
             ('Lithuania', 0.036156656018847114),
             ('Luxembourg', 0.08827699933733259),
             ('Moldova', 0.04057011426747039),
             ('Montenegro', 0.014497424613869882),
             ('Morocco', 0.01395924692014025),
             ('Netherlands', 0.06952839547264533),
             ('North Macedonia', 0.03859960257847538),
             ('Norway', 0.005605852998444943),
             ('Palestine', 0.010712397276272729),
             ('Poland', 0.05863606446298291),
             ('Portugal', 0.03586413967972179),
             ('Romania', 0.043443063612352145),
             ('Russian Federation', 0.018572837395256274),
             ('Saudi Arabia', 0.004704854090017228),
             ('Serbia', 0.03066131382194287),
             ('Slovakia', 0.06210604361588843),
             ('Slovenia', 0.10528170218127014),
             ('Spain', 0.03968266080460739),
             ('Sweden', 0.014314957465463669),
             ('Switzerland', 0.07801704200705196),
             ('Syria', 0.01585247121071788),
             ('Tunisia', 0.008212136788902645),
             ('Turkey', 0.028548454391349884),
             ('Ukraine', 0.03476316636145003),
             ('United Kingdom', 0.019651767304355323)]
winter_ac = np.array(winter_ac)

# =============================================================================
# ------------------------LIST OF EUROPEAN COUNTRIES---------------------------
# =============================================================================

europe = ['Belarus',
          'Belgium',
          'Bosnia and Herzegovina',
          'Bulgaria',
          'Croatia',
          'Cyprus',
          'Czechia',
          'Denmark',
          'Estonia',
          'Faroes',
          'Finland',
          'France',
          'Germany',
          'Greece',
          'Hungary',
          'Iceland',
          'Ireland',
          'Italy',
          'Latvia',
          'Lithuania',
          'Luxembourg',
          'Moldova',
          'Montenegro',
          'Netherlands',
          'North Macedonia',
          'Norway',
          'Poland',
          'Portugal',
          'Romania',
          'Russian Federation',
          'Serbia',
          'Slovakia',
          'Slovenia',
          'Spain',
          'Sweden',
          'Switzerland',
          'Ukraine',
          'United Kingdom']

regions = {"Europe":                ['Belarus',
                      'Belgium',
                      'Bosnia and Herzegovina',
                      'Bulgaria',
                      'Croatia',
                      'Cyprus',
                      'Czechia',
                      'Denmark',
                      'Estonia',
                      'Faroes',
                      'Finland',
                      'France',
                      'Germany',
                      'Greece',
                      'Hungary',
                      'Iceland',
                      'Ireland',
                      'Italy',
                      'Latvia',
                      'Lithuania',
                      'Luxembourg',
                      'Moldova',
                      'Montenegro',
                      'Netherlands',
                      'North Macedonia',
                      'Norway',
                      'Poland',
                      'Portugal',
                      'Romania',
                      'Russian Federation',
                      'Serbia',
                      'Slovakia',
                      'Slovenia',
                      'Spain',
                      'Sweden',
                      'Switzerland',
                      'Ukraine',
                      'United Kingdom'],
           "Western Europe":        ['Belgium',
                              'France',
                              'Ireland',
                              'Netherlands',
                              'United Kingdom'],
           "Central Europe":        ['Croatia',
                              'Czechia',
                              'Estonia',
                              'Germany',
                              'Hungary',
                              'Latvia',
                              'Lithuania',
                              'Luxembourg',
                              'Poland',
                              'Slovakia',
                              'Slovenia',
                              'Switzerland',],
           "Eastern Europe":        ['Belarus',
                              'Russian Federation',
                              'Ukraine',],
           "Southern Europe":       ['Italy',
                               'Portugal',
                               'Spain',],
           "Southeastern Europe":   ['Bosnia and Herzegovina',
                                   'Bulgaria',
                                   'Cyprus',
                                   'Greece',
                                   'Moldova',
                                   'Montenegro',
                                   'North Macedonia',
                                   'Romania',
                                   'Serbia',],
           "Northern Europe":       ['Denmark',
                               'Faroes',
                               'Finland',
                               'Iceland',
                               "Sweden",
                               'Norway',
                               'Sweden',]}

# =============================================================================
# Initialize arrays to store ratio and percentage
val_arr = []
perc_arr_named = []
perc_arr_val = []
val = 0
adj = 1

# =============================================================================
# --------------------------------USER-INPUT-----------------------------------
# =============================================================================
# Select arrays to be used:

sel_winter = np.array([('Albania', 0.029744859137458498),
             ('Algeria', 0.008863826641201123),
             ('Armenia', 0.035123795832261606),
             ('Austria', 0.08022019454575562),
             ('Azerbaijan', 0.03208444000454896),
             ('Belarus', 0.03761542823864437),
             ('Belgium', 0.07657769246820342),
             ('Bosnia and Herzegovina', 0.03464149869918198),
             ('Bulgaria', 0.02278757643565538),
             ('Croatia', 0.0643934698926948),
             ('Cyprus', 0.008554231552850632),
             ('Czechia', 0.0766477368756012),
             ('Denmark', 0.04831800900431944),
             ('Egypt', 0.006359758831205823),
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
             ('Ireland', 0.008366256694747741),
             ('Israel', 0.015961076668531266),
             ('Italy', 0.06783644657053384),
             ('Jordan', 0.00915364057526803),
             ('Kazakhstan', 0.009988338893356659),
             ('Latvia', 0.025563785043323226),
             ('Lebanon', 0.024242223888014804),
             ('Libya', 0.004498385669318381),
             ('Lithuania', 0.036156656018847114),
             ('Luxembourg', 0.08827699933733259),
             ('Moldova', 0.04057011426747039),
             ('Montenegro', 0.014497424613869882),
             ('Morocco', 0.01395924692014025),
             ('Netherlands', 0.06952839547264533),
             ('North Macedonia', 0.03859960257847538),
             ('Norway', 0.005605852998444943),
             ('Palestine', 0.010712397276272729),
             ('Poland', 0.05863606446298291),
             ('Portugal', 0.03586413967972179),
             ('Romania', 0.043443063612352145),
             ('Russian Federation', 0.018572837395256274),
             ('Saudi Arabia', 0.004704854090017228),
             ('Serbia', 0.03066131382194287),
             ('Slovakia', 0.06210604361588843),
             ('Slovenia', 0.10528170218127014),
             ('Spain', 0.03968266080460739),
             ('Sweden', 0.014314957465463669),
             ('Switzerland', 0.07801704200705196),
             ('Syria', 0.01585247121071788),
             ('Tunisia', 0.008212136788902645),
             ('Turkey', 0.028548454391349884),
             ('Ukraine', 0.03476316636145003),
             ('United Kingdom', 0.019651767304355323)])
sel_summer = np.array([('Albania', 0.016983942252075473),
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

# If you are calculating a summer to winter ratio, set ratio to true:
ratio = True

# Set whether you want the outcomes in percentages (ratio = True):
percent = True

# Set division order (ratio = True):
summer_divby_winter = True

# Set season (ratio = False):
win = True

# Select european countries only or whole dataset:
european_only = True

# Decimals:
dec = 4

# Number of standard deviations for outlier bounds
sd_m = 2

# =============================================================================
# -----------------------------------------------------------------------------
# =============================================================================
# Calculate ratios and percentages

coher = 0

for i in range(len(sel_winter)):
    # Check if list items are coherent
    if sel_winter[i, 0] != sel_summer[i, 0]:
        coher += 1

    if european_only:
        if sel_winter[i, 0] in europe:
            if ratio:
                if summer_divby_winter:
                    val = float(sel_summer[i, 1]) / float(sel_winter[i, 1]) - adj
                    val_arr.append([sel_summer[i, 0], val])
                    if percent:
                        perc_arr_named.append([sel_winter[i, 0], round(val * 100, dec)])
                        perc_arr_val.append(val * 100)
                else:
                    val = float(sel_winter[i, 1]) / float(sel_summer[i, 1]) - adj
                    val_arr.append([sel_summer[i, 0], val])
                    if percent:
                        perc_arr_named.append([sel_winter[i, 0], round(val * 100, dec)])
                        perc_arr_val.append(val * 100)
            else:
                if win:
                    val = float(sel_winter[i, 1])
                    val_arr.append([sel_winter[i, 0], val])
                    perc_arr_val.append(val)
                    perc_arr_named.append([sel_winter[i, 0], val])
                else:
                    val = float(sel_summer[i, 1])
                    val_arr.append([sel_summer[i, 0], val])
                    perc_arr_val.append(val)
                    perc_arr_named.append([sel_summer[i, 0], val])
    else:
        if ratio:
            # Divide values of different seasons
            if summer_divby_winter:
                val = float(sel_summer[i, 1]) / float(sel_winter[i, 1]) - adj
                val_arr.append([sel_summer[i, 0], val])
                if percent:
                    perc_arr_named.append([sel_winter[i, 0], round(val * 100, dec)])
                    perc_arr_val.append(val * 100)
            else:
                val = float(sel_winter[i, 1]) / float(sel_summer[i, 1]) - adj
                val_arr.append([sel_summer[i, 0], val])
                if percent:
                    perc_arr_named.append([sel_winter[i, 0], round(val * 100, dec)])
                    perc_arr_val.append(val * 100)
        else:
            if win:
                val = float(sel_winter[i, 1])
                val_arr.append([sel_winter[i, 0], val])
                perc_arr_val.append(val)
                perc_arr_named.append([sel_winter[i, 0], val])
            else:
                val = float(sel_summer[i, 1])
                val_arr.append([sel_summer[i, 0], val])
                perc_arr_val.append(val)
                perc_arr_named.append([sel_summer[i, 0], val])

if coher == 0:
    print("NO ARRAY COHERENCE ERRORS")
else:
    print("ERROR! " + str(coher) + "ARRAY ENTRIES NOT COHERENT")

# =============================================================================
# Print info about set:

print('Europe only: ' + str(european_only))
print()

# Print ratio array in a nice way
# pp = PrettyPrinter(indent=4)
# pp.pprint(perc_arr_named)

# ==============================================================================

# Splitting data into 3 arrays for more info
# Lower array contains values below (sd_m) number of std. devs. (low fliers)
# Upper array contains values above (sd_m) number of std. devs. (high fliers)
split_low = []
split_upp = []
split_mid = []

named_low = []
named_mid = []
named_upp = []

# print("Region:", region)
# regional_perc_arr_named = [country for country in perc_arr_named if country[0] in regions[region]]
# regional_perc_arr_val = [country[1] for country in regional_perc_arr_named]
# print("regional_perc_arr_val", regional_perc_arr_val)
data_mean = np.mean(perc_arr_val)
data_sd = stats.stdev(perc_arr_val)

high_outliers = []
low_outliers = []

print('Outlier bounds: ' + str(round(data_mean - sd_m * data_sd, dec)) + ', ' + str(
    round(data_mean + sd_m * data_sd, dec)))

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
print()

# =======================================================================================
# Calculate stat data for split arrays
main_mean = np.mean(perc_arr_val)
main_sd = stats.stdev(perc_arr_val)
main_median = stats.median(perc_arr_val)

# Print stat data nicely (some debugging included)
print('TOT: MEAN = ' + str(np.round(main_mean, dec)) + ' SD = ' + str(round(main_sd, dec)))
print()

if len(split_low) > 2:
    low_mean = np.mean(split_low)
    low_sd = stats.stdev(split_low)
    print('LOW: MEAN = ' + str(np.round(low_mean, dec)) + ' SD = ' + str(round(low_sd, dec)))

mid_mean = np.mean(split_mid)
mid_sd = stats.stdev(split_mid)
print('MID: MEAN = ' + str(np.round(mid_mean, dec)) + ' SD = ' + str(round(mid_sd, dec)))

if len(split_upp) > 2:
    upp_mean = np.mean(split_upp)
    upp_sd = stats.stdev(split_upp)
    print('UPP: MEAN = ' + str(np.round(upp_mean, dec)) + ' SD = ' + str(round(upp_sd, dec)))

# Remind you that you set it to percentages
if percent:
    print()
    print('(Unit: %)')

# =================================================================================
# Make boxplot

fig, axs = plt.subplots()

# data = [split_low, split_upp]
data = perc_arr_val

bp = axs.boxplot(data, vert=False, showmeans=True, meanline=True)

maxval = round(np.max(perc_arr_val), dec)
minval = round(np.min(perc_arr_val), dec)

major = maxval / 10
minor = maxval / 50

major_ticks = np.arange(minval, maxval, major)
minor_ticks = np.arange(minval, maxval, minor)
axs.set_xticks(major_ticks)
axs.set_xticks(minor_ticks, minor=True)

axs.grid(which='minor', alpha=0.2)
axs.grid(which='major', alpha=0.5)

axs.set_yticks([])

# plt.title('% Summer to winter aircraft-attributable PM2.5')

plt.tight_layout()
# plt.show()

