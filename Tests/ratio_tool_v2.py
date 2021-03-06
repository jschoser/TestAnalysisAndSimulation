import numpy as np
from pprint import PrettyPrinter
import matplotlib.pyplot as plt
import statistics as stats


# =========================== FINE PARTICULATE MATTER =========================
# =============================================================================
# ---------------------------------BG_PM25_JAN---------------------------------
# =============================================================================

bg_pm25_jan = [('Albania', 18.550506668010833),
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
bg_pm25_jan = np.array(bg_pm25_jan)


# =============================================================================
# --------------------------------BG_PM25_JULY---------------------------------
# =============================================================================

bg_pm25_july = [('Albania', 11.008944668602071),
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
bg_pm25_july = np.array(bg_pm25_july)

# =============================================================================
# -------------------------------AC_PM25_JAN-----------------------------------
# =============================================================================

ac_pm25_jan = [('Albania', 0.029744859137458498),
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
ac_pm25_jan = np.array(ac_pm25_jan)


# =============================================================================
# --------------------------------AC_PM25_JULY---------------------------------
# =============================================================================

ac_pm25_july = [('Albania', 0.016983942252075473),
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
ac_pm25_july = np.array(ac_pm25_july)

# ================================= OZONE =====================================
# =============================================================================
# --------------------------------BG_O3_JAN------------------------------------
# =============================================================================

bg_o3_jan = [   ('Albania', 23.79807385524294),
    ('Algeria', 32.50079722827548),
    ('Armenia', 36.1120683038239),
    ('Austria', 17.68771624179858),
    ('Azerbaijan', 30.685663548615317),
    ('Belarus', 13.74569125688426),
    ('Belgium', 9.562557912471727),
    ('Bosnia and Herzegovina', 18.476825169271475),
    ('Bulgaria', 18.69251707969231),
    ('Croatia', 17.58877631882938),
    ('Cyprus', 35.07277290462673),
    ('Czechia', 11.34032836577722),
    ('Denmark', 15.947469588643203),
    ('Egypt', 34.30981264175768),
    ('Estonia', 13.499597122615482),
    ('Faroes', 28.15720232632552),
    ('Finland', 15.42148634190227),
    ('France', 18.469338857007237),
    ('Georgia', 34.796586110407716),
    ('Germany', 10.12787718284134),
    ('Greece', 24.93690713665483),
    ('Hungary', 11.430537372178016),
    ('Iceland', 27.07310552571003),
    ('Iran', 35.07934590138949),
    ('Iraq', 32.8896153220955),
    ('Ireland', 26.56827769046382),
    ('Israel', 29.738927039519005),
    ('Italy', 21.334165841564598),
    ('Jordan', 33.62760962255924),
    ('Kazakhstan', 19.403678572169067),
    ('Latvia', 13.532529644183452),
    ('Lebanon', 30.49097265139594),
    ('Libya', 32.80308607300101),
    ('Lithuania', 13.672118715989834),
    ('Luxembourg', 8.569085843018478),
    ('Moldova', 14.735780275944135),
    ('Montenegro', 23.4373864579815),
    ('Morocco', 33.84613604417662),
    ('Netherlands', 12.248499984079604),
    ('North Macedonia', 18.399275824174225),
    ('Norway', 23.277069530595355),
    ('Palestine', 26.088089169038184),
    ('Poland', 10.976923041377725),
    ('Portugal', 25.636286463924247),
    ('Romania', 16.120184382202805),
    ('Russian Federation', 17.6101053064804),
    ('Saudi Arabia', 35.89478255209045),
    ('Serbia', 14.675366129551218),
    ('Slovakia', 11.3558901353917),
    ('Slovenia', 15.641227278928046),
    ('Spain', 26.348164933184123),
    ('Sweden', 19.50846371945968),
    ('Switzerland', 22.123850116815383),
    ('Syria', 31.157752416917397),
    ('Tunisia', 31.183872690961227),
    ('Turkey', 31.59609782087539),
    ('Ukraine', 14.265947845987236),
    ('United Kingdom', 21.602326638392753)]
bg_o3_jan = np.array(bg_o3_jan)

# =============================================================================
# --------------------------------BG_O3_JULY-----------------------------------
# =============================================================================

bg_o3_july = [   ('Albania', 57.035506105021554),
    ('Algeria', 44.77287935754137),
    ('Armenia', 61.845086648777084),
    ('Austria', 51.18698673915308),
    ('Azerbaijan', 57.78965406587473),
    ('Belarus', 44.68263547473729),
    ('Belgium', 38.478536892520005),
    ('Bosnia and Herzegovina', 53.057578393133895),
    ('Bulgaria', 53.30075315486642),
    ('Croatia', 54.767164348976706),
    ('Cyprus', 60.48433187104474),
    ('Czechia', 48.037524526887104),
    ('Denmark', 38.47571674460606),
    ('Egypt', 53.2254137483722),
    ('Estonia', 38.742967818777345),
    ('Faroes', 28.873900889663354),
    ('Finland', 32.406199865009256),
    ('France', 45.01183202792922),
    ('Georgia', 52.46415111632082),
    ('Germany', 43.17616335536959),
    ('Greece', 57.05006537642347),
    ('Hungary', 52.531375414983394),
    ('Iceland', 26.037770251743137),
    ('Iran', 64.93175573798986),
    ('Iraq', 63.72771988620042),
    ('Ireland', 31.41364494672505),
    ('Israel', 51.00997676931645),
    ('Italy', 56.63703965721515),
    ('Jordan', 57.031041331839845),
    ('Kazakhstan', 46.30733478272579),
    ('Latvia', 38.775912380977225),
    ('Lebanon', 56.67239155749759),
    ('Libya', 50.806203337521154),
    ('Lithuania', 41.22456445329194),
    ('Luxembourg', 42.92293657012383),
    ('Moldova', 50.28874533786256),
    ('Montenegro', 54.54829966021124),
    ('Morocco', 40.53940867886472),
    ('Netherlands', 36.33505357701112),
    ('North Macedonia', 55.291144999595296),
    ('Norway', 32.4383099472535),
    ('Palestine', 44.920447925154406),
    ('Poland', 46.48377299044559),
    ('Portugal', 43.033625412623074),
    ('Romania', 51.112365270708274),
    ('Russian Federation', 39.71672305268076),
    ('Saudi Arabia', 59.65868152480836),
    ('Serbia', 52.57945953958372),
    ('Slovakia', 50.90763087409577),
    ('Slovenia', 55.27285591113581),
    ('Spain', 49.9527641388853),
    ('Sweden', 32.449046030328425),
    ('Switzerland', 51.10148167272123),
    ('Syria', 59.200542813463144),
    ('Tunisia', 49.933119714703366),
    ('Turkey', 58.359330657195656),
    ('Ukraine', 48.78094811962862),
    ('United Kingdom', 31.459539436663725)]
bg_o3_july = np.array(bg_o3_july)

# =============================================================================
# --------------------------------AC_O3_JAN------------------------------------
# =============================================================================

ac_o3_jan = [   ('Albania', 0.2527610203244782),
    ('Algeria', 0.2971892001291221),
    ('Armenia', 0.3856691338840272),
    ('Austria', 0.21607114893376264),
    ('Azerbaijan', 0.2961535531107132),
    ('Belarus', 0.1717562617524636),
    ('Belgium', 0.13343572577456497),
    ('Bosnia and Herzegovina', 0.2155911858994957),
    ('Bulgaria', 0.21335681707440698),
    ('Croatia', 0.202900504554567),
    ('Cyprus', 0.2825380141487022),
    ('Czechia', 0.16331977903852607),
    ('Denmark', 0.20127773788701833),
    ('Egypt', 0.3020711723084311),
    ('Estonia', 0.1742607215264713),
    ('Faroes', 0.2768131964070497),
    ('Finland', 0.19429454174778935),
    ('France', 0.2072648222315861),
    ('Georgia', 0.3613739177135768),
    ('Germany', 0.15103845702751528),
    ('Greece', 0.26206600384150724),
    ('Hungary', 0.14941688956878688),
    ('Iceland', 0.27033976655846825),
    ('Iran', 0.33908313695301895),
    ('Iraq', 0.23709612370960562),
    ('Ireland', 0.2518144698933176),
    ('Israel', 0.2776329161950804),
    ('Italy', 0.24320995029172804),
    ('Jordan', 0.26175142969722404),
    ('Kazakhstan', 0.16758674452042593),
    ('Latvia', 0.1746133149610697),
    ('Lebanon', 0.29379161001016435),
    ('Libya', 0.28770745371915984),
    ('Lithuania', 0.1751980242399168),
    ('Luxembourg', 0.11165639841286586),
    ('Moldova', 0.16835402647506661),
    ('Montenegro', 0.24399124277496864),
    ('Morocco', 0.3432923696302007),
    ('Netherlands', 0.14913001355740568),
    ('North Macedonia', 0.225055150876154),
    ('Norway', 0.25307997323043674),
    ('Palestine', 0.25303022226473854),
    ('Poland', 0.15652835333552753),
    ('Portugal', 0.25530229261559717),
    ('Romania', 0.18682230099087047),
    ('Russian Federation', 0.19223635127175664),
    ('Saudi Arabia', 0.2504092343385813),
    ('Serbia', 0.18247087852183905),
    ('Slovakia', 0.15705373228547134),
    ('Slovenia', 0.20776277629624576),
    ('Spain', 0.26159815561726946),
    ('Sweden', 0.22664214331794139),
    ('Switzerland', 0.2832941196404456),
    ('Syria', 0.23165379167839495),
    ('Tunisia', 0.2581965667441654),
    ('Turkey', 0.28574189383379267),
    ('Ukraine', 0.16799390453792476),
    ('United Kingdom', 0.2277350201044282)]
ac_o3_jan = np.array(ac_o3_jan)

# =============================================================================
# --------------------------------AC_O3_JULY-----------------------------------
# =============================================================================

ac_o3_july = [   ('Albania', 0.33840339041704437),
    ('Algeria', 0.2790512856217763),
    ('Armenia', 0.2530433698354555),
    ('Austria', 0.2622818719331033),
    ('Azerbaijan', 0.16888031725303052),
    ('Belarus', 0.18759831517846096),
    ('Belgium', 0.12002119524760321),
    ('Bosnia and Herzegovina', 0.28462829964876685),
    ('Bulgaria', 0.2833856242806527),
    ('Croatia', 0.25350515341985597),
    ('Cyprus', 0.3411333155991232),
    ('Czechia', 0.23121917918938614),
    ('Denmark', 0.08232946183316485),
    ('Egypt', 0.25746177676583537),
    ('Estonia', 0.146236835702555),
    ('Faroes', 0.0547385047560024),
    ('Finland', 0.13528457292482368),
    ('France', 0.1768779789581737),
    ('Georgia', 0.25221953502930256),
    ('Germany', 0.16299307420889567),
    ('Greece', 0.29824195652435265),
    ('Hungary', 0.2455145424601609),
    ('Iceland', 0.06536676584682223),
    ('Iran', 0.3522751067150056),
    ('Iraq', 0.4241161961291844),
    ('Ireland', 0.07823478726890452),
    ('Israel', 0.2870542486361998),
    ('Italy', 0.27661709688672287),
    ('Jordan', 0.363377117021181),
    ('Kazakhstan', 0.1975033465681764),
    ('Latvia', 0.14319990678337105),
    ('Lebanon', 0.3807792405944649),
    ('Libya', 0.27803407174845063),
    ('Lithuania', 0.15635048290136744),
    ('Luxembourg', 0.15810844696976087),
    ('Moldova', 0.2494857452062886),
    ('Montenegro', 0.33737345817578707),
    ('Morocco', 0.16737405615304238),
    ('Netherlands', 0.0680296719053154),
    ('North Macedonia', 0.3414803030505206),
    ('Norway', 0.11476167273777896),
    ('Palestine', 0.2548958532944623),
    ('Poland', 0.19301513058056705),
    ('Portugal', 0.14076755356902035),
    ('Romania', 0.2616659635329372),
    ('Russian Federation', 0.18604141042004055),
    ('Saudi Arabia', 0.3950594969211239),
    ('Serbia', 0.29771167509655755),
    ('Slovakia', 0.24046170915418077),
    ('Slovenia', 0.2230847020055087),
    ('Spain', 0.2204956709402732),
    ('Sweden', 0.13157669229320215),
    ('Switzerland', 0.27749203038482473),
    ('Syria', 0.39415075899464025),
    ('Tunisia', 0.28129365186911676),
    ('Turkey', 0.3902358843404462),
    ('Ukraine', 0.23260180308439227),
    ('United Kingdom', 0.05352092911246939)]
ac_o3_july = np.array(ac_o3_july)

# =============================================================================
# ------------------------LIST OF EUROPEAN COUNTRIES---------------------------
# =============================================================================

regions = {"Europe": ['Belarus',
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
           "Western Europe": ['Belgium',
                              'France',
                              'Ireland',
                              'Netherlands',
                              'United Kingdom'],
           "Central Europe": ['Croatia',
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
                              'Switzerland'],
           "Eastern Europe": ['Belarus',
                              'Russian Federation',
                              'Ukraine'],
           "Southern Europe": ['Italy',
                               'Portugal',
                               'Spain'],
           "Southeastern Europe": ['Bosnia and Herzegovina',
                                   'Bulgaria',
                                   'Cyprus',
                                   'Greece',
                                   'Moldova',
                                   'Montenegro',
                                   'North Macedonia',
                                   'Romania',
                                   'Serbia'],
           "Northern Europe": ['Denmark',
                               'Faroes',
                               'Finland',
                               'Iceland',
                               "Sweden",
                               'Norway',
                               'Sweden'],
           "C,E,SE": ['Croatia',
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
                      'Switzerland',
                      'Belarus',
                      'Russian Federation',
                      'Ukraine',
                      'Bosnia and Herzegovina',
                      'Bulgaria',
                      'Cyprus',
                      'Greece',
                      'Moldova',
                      'Montenegro',
                      'North Macedonia',
                      'Romania',
                      'Serbia']}

# =============================================================================
# --------------------------------USER-INPUT-----------------------------------
# =============================================================================
# Select arrays to be used:

sel_winter = bg_o3_jan
sel_summer = bg_o3_july

# If you are calculating a summer to winter ratio, set ratio to true:
ratio = False

# Set division order (ratio = True):
summer_divby_winter = False

# Set season (ratio = False):
win = False

# Decimals of output:
dec = 2

# Set if you want contribution of aviation-attributable emission of total
contribution = True
# Number of standard deviations for outlier bounds
# sd_m = 2

# =============================================================================
# Check coherence of summer and winter arrays:

coher = 0

for i in range(len(sel_winter)):
    # Check if list items are coherent
    if sel_winter[i, 0] != sel_summer[i, 0]:
        coher += 1

if coher == 0:
    print("NO ARRAY COHERENCE ERRORS")
else:
    print("ERROR! " + str(coher) + "ARRAY ENTRIES NOT COHERENT")
print()
# =============================================================================
# Calculate stat data for each region:

if ratio:
    for region in regions:
        val_arr = []
        named_arr = []
        for i in range(len(sel_summer)):
            if sel_summer[i, 0] in regions[region]:
                if summer_divby_winter:
                    val = float(sel_summer[i, 1]) / float(sel_winter[i, 1]) - 1
                else:
                    val = float(sel_winter[i, 1]) / float(sel_summer[i, 1]) - 1
                named_arr.append([sel_summer[i, 0], val * 100])
                val_arr.append(val * 100)
        mean = np.mean(val_arr)
        stdev = stats.stdev(val_arr)
        print(region + ": MEAN = " + str(round(mean, dec)) + " (SD = " + str(round(stdev, dec)) + ")")
    print()
    print("Values in percent")
else:
    if win:
        select = sel_winter
    else:
        select = sel_summer
    for region in regions:
        val_arr = []
        named_arr = []
        for i in range(len(select)):
            if select[i, 0] in regions[region]:
                val = float(select[i, 1])
                named_arr.append([select[i, 0], val])
                val_arr.append(val)
        mean = np.mean(val_arr)
        stdev = stats.stdev(val_arr)
        print(region + ": MEAN = " + str(round(mean, dec)) + " (SD = " + str(round(stdev, dec)) + ")")
    print()
    print("Winter: " + str(win))

if contribution:
    print()
    print("Contribution of aviation-attributable pollutant vs background")
    for region in regions:
        val_arr = []
        named_arr = []
        for i in range(len(sel_summer)):
            if sel_summer[i, 0] in regions[region]:
                val = float(ac_pm25_jan[i, 1]) / float(bg_pm25_jan[i, 1])
                named_arr.append([sel_summer[i, 0], val * 100])
                val_arr.append(val * 100)
        mean = np.mean(val_arr)
        stdev = stats.stdev(val_arr)
        print(region + ": MEAN = " + str(round(mean, dec)) + " (SD = " + str(round(stdev, dec)) + ")")
    print()
    print("Values in percent")


