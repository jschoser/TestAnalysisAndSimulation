import numpy as np
from pprint import PrettyPrinter
import matplotlib.pyplot as plt
import statistics as stats

# =============================================================================
# ---------------------------SUMMER BACKGROUND---------------------------------
# =============================================================================

summer_bg = [   ('Albania', 11.008944668602071),
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

winter_bg = [   ('Albania', 18.550506668010833),
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
# ----------------------------SUMMER AC/BASE RATIO-----------------------------
# =============================================================================

summer_ratio = [('Albania', 0.001675916162113695),
                ('Algeria', 0.0008644157328294542),
                ('Armenia', 0.0008359361319928465),
                ('Austria', 0.0037956402096044643),
                ('Azerbaijan', 0.0005446900490606215),
                ('Belarus', 0.0016811065436374343),
                ('Belgium', 0.003420755599204242),
                ('Bosnia and Herzegovina', 0.0018769246686361866),
                ('Bulgaria', 0.0012272384682785913),
                ('Croatia', 0.0018413176254497062),
                ('Cyprus', 0.0012903345364426808),
                ('Czechia', 0.00314280386423541),
                ('Denmark', 0.0011890005679936627),
                ('Egypt', 0.0013239309413447268),
                ('Estonia', 0.0012217997331320162),
                ('Faroes', 0.000244213326936437),
                ('Finland', 0.00104679637038478),
                ('France', 0.002284544397254371),
                ('Georgia', 0.0010528726423839152),
                ('Germany', 0.0031949545606301815),
                ('Greece', 0.0010868893999721521),
                ('Hungary', 0.0023064935736031578),
                ('Iceland', 0.0003390614196663385),
                ('Iran', 0.0008937247672981769),
                ('Iraq', 0.0008835171006022003),
                ('Ireland', 0.0018818196001909684),
                ('Israel', 0.0013221269684210038),
                ('Italy', 0.0024867883311529703),
                ('Jordan', 0.0010785781755348661),
                ('Kazakhstan', 0.0008368675694768),
                ('Latvia', 0.0014087256543945537),
                ('Lebanon', 0.001551551045459998),
                ('Libya', 0.001161739913127304),
                ('Lithuania', 0.0016598308914019721),
                ('Luxembourg', 0.003564538345450447),
                ('Moldova', 0.0014429344712764958),
                ('Montenegro', 0.0016806437071907978),
                ('Morocco', 0.0005892335253937508),
                ('Netherlands', 0.0027182070839108976),
                ('North Macedonia', 0.001283117098445443),
                ('Norway', 0.0008924008737911036),
                ('Palestine', 0.0009086757007515921),
                ('Poland', 0.001968442509159455),
                ('Portugal', 0.0006230260592932776),
                ('Romania', 0.001822773497211122),
                ('Russian Federation', 0.0011302068001343322),
                ('Saudi Arabia', 0.00101300230225533),
                ('Serbia', 0.0013531504097296781),
                ('Slovakia', 0.0023502659396453913),
                ('Slovenia', 0.0022602731645238274),
                ('Spain', 0.0011785746515171453),
                ('Sweden', 0.0011880223456410138),
                ('Switzerland', 0.004511990313033526),
                ('Syria', 0.0011244381305450211),
                ('Tunisia', 0.001073582785450781),
                ('Turkey', 0.0014130446853165776),
                ('Ukraine', 0.0013579222518754245),
                ('United Kingdom', 0.001354047731630932)]
summer_ratio = np.array(summer_ratio)

# =============================================================================
# ----------------------------WINTER AC/BASE RATIO-----------------------------
# =============================================================================

winter_ratio = [('Albania', 0.001640632903702775),
                ('Algeria', 0.001331997731616937),
                ('Armenia', 0.002091461563206818),
                ('Austria', 0.004158260348429778),
                ('Azerbaijan', 0.0015740231963728912),
                ('Belarus', 0.0014133553373979382),
                ('Belgium', 0.0027927336017641224),
                ('Bosnia and Herzegovina', 0.0016398539340598997),
                ('Bulgaria', 0.0009356417803345531),
                ('Croatia', 0.002328388251636796),
                ('Cyprus', 0.0008516604346888408),
                ('Czechia', 0.0029749492120610716),
                ('Denmark', 0.002959653543006997),
                ('Egypt', 0.000796757283664885),
                ('Estonia', 0.0009401072279946222),
                ('Faroes', 0.0004240069322115602),
                ('Finland', 0.0008785235478270873),
                ('France', 0.0032673559044391243),
                ('Georgia', 0.0017911894833258588),
                ('Germany', 0.003621642543801573),
                ('Greece', 0.0010664261485843157),
                ('Hungary', 0.002434320981780669),
                ('Iceland', 0.00034590550422060876),
                ('Iran', 0.002147463064507136),
                ('Iraq', 0.0008602360980081045),
                ('Ireland', 0.0013343472145249033),
                ('Israel', 0.0010259065910561715),
                ('Italy', 0.0034607041352869472),
                ('Jordan', 0.0007494801553734548),
                ('Kazakhstan', 0.000611972358183691),
                ('Latvia', 0.0010977871757623771),
                ('Lebanon', 0.001612199223264622),
                ('Libya', 0.0006536432119165017),
                ('Lithuania', 0.0014960778112136706),
                ('Luxembourg', 0.002959105230513073),
                ('Moldova', 0.0013252733038309561),
                ('Montenegro', 0.0009197647816129613),
                ('Morocco', 0.0022076226010709515),
                ('Netherlands', 0.0032668837010311658),
                ('North Macedonia', 0.0013919947875937106),
                ('Norway', 0.0008676648468171815),
                ('Palestine', 0.0007128494125666569),
                ('Poland', 0.002202105360428232),
                ('Portugal', 0.0028689880387269004),
                ('Romania', 0.0014592210090255276),
                ('Russian Federation', 0.000893232654085418),
                ('Saudi Arabia', 0.0005426951325895436),
                ('Serbia', 0.001127931104387255),
                ('Slovakia', 0.002035310441423148),
                ('Slovenia', 0.003593870176557914),
                ('Spain', 0.003221710003417401),
                ('Sweden', 0.0012317771714010059),
                ('Switzerland', 0.004694782503469242),
                ('Syria', 0.0010110522203154667),
                ('Tunisia', 0.0008686296554189561),
                ('Turkey', 0.0015227056607562976),
                ('Ukraine', 0.0012710129347190855),
                ('United Kingdom', 0.0018667116367255853)]
winter_ratio = np.array(winter_ratio)

# =============================================================================
# ------------------------LIST OF EUROPEAN COUNTRIES---------------------------
# =============================================================================

europe =    [   'Belarus',
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

# =============================================================================

# Initialize arrays to store ratio and percentage
val_arr = []
perc_arr_named = []
perc_arr_val = []
tot = 0
val = 0

# =============================================================================

# Select arrays to be used:

sel_winter = winter_ratio
sel_summer = summer_ratio

# If you are calculating a summer to winter ratio, set to true, set whether you want percentages and set order:
ratio = False
percent = True
summer_divby_winter = True

# If not calculating a ratio, set season:
win = False

# Select only european countries or whole dataset:
european_only = True
SPECIFIC = ['Denmark', 'Faroes', 'Greece', 'United Kingdom']

# Adjust ratios to better show decrease:
adj = 1

# Decimals:
dec = 4

# =============================================================================

# Calculate ratios and percentages

for i in range(len(sel_winter)):
    if european_only:
        if sel_winter[i, 0] in europe:
            if sel_winter[i, 0] != sel_summer[i, 0]:
                print('ERROR: ARRAY ELEMENTS (index = ' + str(i) + ' ) NOT COHERENT')

            if ratio:
                if summer_divby_winter:
                    val = float(sel_summer[i, 1]) / float(sel_winter[i, 1]) - adj
                    if percent:
                        perc_arr_named.append([sel_winter[i, 0], round(val * 100, dec)])
                        perc_arr_val.append(val * 100)
                else:
                    val = float(sel_winter[i, 1]) / float(sel_summer[i, 1]) - adj
                    if percent:
                        perc_arr_named.append([sel_winter[i, 0], round(val * 100, dec)])
                        perc_arr_val.append(val * 100)
            else:
                if win:
                    val = float(sel_winter[i, 1])
                    val_arr.append([sel_winter[i, 0], val])
                    if percent:
                        perc_arr_named.append([sel_winter[i, 0], round(val * 100, dec)])
                        perc_arr_val.append(val * 100)

                else:
                    val = float(sel_summer[i, 1])
                    val_arr.append([sel_summer[i, 0], val])
                    if percent:
                        perc_arr_named.append([sel_summer[i, 0], round(val * 100, dec)])
                        perc_arr_val.append(val * 100)
    else:
        if sel_winter[i, 0]:
            if sel_winter[i, 0] != sel_summer[i, 0]:
                print('ERROR: ARRAY ELEMENTS (index = ' + str(i) + ' ) NOT COHERENT')

            if ratio:
                if summer_divby_winter:
                    val = float(sel_summer[i, 1]) / float(sel_winter[i, 1]) - adj
                    if percent:
                        perc_arr_named.append([sel_winter[i, 0], round(val * 100, dec)])
                        perc_arr_val.append(val * 100)
                else:
                    val = float(sel_winter[i, 1]) / float(sel_summer[i, 1]) - adj
                    if percent:
                        perc_arr_named.append([sel_winter[i, 0], round(val * 100, dec)])
                        perc_arr_val.append(val * 100)
            else:
                if win:
                    val = float(sel_winter[i, 1])
                    val_arr.append([sel_winter[i, 0], val])
                    if percent:
                        perc_arr_named.append([sel_winter[i, 0], round(val * 100, dec)])
                        perc_arr_val.append(val * 100)

                else:
                    val = float(sel_summer[i, 1])
                    val_arr.append([sel_summer[i, 0], val])
                    if percent:
                        perc_arr_named.append([sel_summer[i, 0], round(val * 100, dec)])
                        perc_arr_val.append(val * 100)

    tot += val

if not percent:
    perc_arr_val = val_arr[:, 1]
    perc_arr_named = val_arr

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
sd_m = 1  # number of standard deviations for outlier bounds

high_outliers = []
low_outliers = []

print('Outlier bounds: ' + str(round(data_mean - sd_m * data_sd, dec)) + ', ' + str(round(data_mean + sd_m * data_sd, dec)))

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

print('TOTAL: MEAN = ' + str(round(main_mean, dec)) + ' SD = ' + str(round(main_sd, dec)) \
      + ' MEDIAN = ' + str(round(main_median, dec)))

if len(split_low) > 2:
    low_mean = np.mean(split_low)
    low_sd = stats.stdev(split_low)
    print('LOW: MEAN = ' + str(round(low_mean, dec)) + ' SD = ' + str(round(low_sd, dec)))

mid_mean = np.mean(split_mid)
mid_sd = stats.stdev(split_mid)
print('MID: MEAN = ' + str(round(mid_mean, dec)) + ' SD = ' + str(round(mid_sd, dec)))

if len(split_upp) > 2:
    upp_mean = np.mean(split_upp)
    upp_sd = stats.stdev(split_upp)
    print('UPP: MEAN = ' + str(round(upp_mean, dec)) + ' SD = ' + str(round(upp_sd, dec)))

# =================================================================================

# Make boxplot

fig, axs = plt.subplots()

# data = [split_low, split_upp]
data = perc_arr_val

bp = axs.boxplot(data, vert=False, showmeans=True, meanline=True)

maxval = round(np.max(perc_arr_val), dec)

major_ticks = np.arange(0, maxval, 50)
minor_ticks = np.arange(0, maxval, 10)
axs.set_xticks(major_ticks)
axs.set_xticks(minor_ticks, minor=True)

axs.grid(which='minor', alpha=0.2)
axs.grid(which='major', alpha=0.5)

axs.set_yticks([])

# plt.title('% Summer to winter aircraft-attributable PM2.5')

plt.tight_layout()
# plt.show()
