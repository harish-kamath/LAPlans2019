# import gmplot package
import gmplot
import os
import googlemaps

marker_size = 40

AirBNBLoc = (34.0434835,-118.2948073)

ERROR_ONES = '''
Prince of Venice food truck
MILK
'''

# RED = LOCATIONS, BLUE = FOOD, GREEN = DESSERT

locations_list = '''West Hollywood Sunset Strip
Arts District
Design District
Hollywood boulevard and Walk of Fame
TCL China Threatre
LACMA
Chinatown
Koreatown
Griffith Observatory
Universal Studios
City Walk
Venice Boardwalk
 Rodeo Drive
 Venice Boardwalk and Canals
 Grand Central Market
 Koreatown
 OUE Skyspace LA
 BROAD Museum
 Beverly Hills
 Olvera Street
 Bradbury Building
 Angel's Flight
 The Last Bookstore
 Intercontinental Hotel
 Smorgasburg
 LA City Hall
 Farmer's Market'''.split("\n")

food_list = '''Poppy and Rose
The Exchange Restaurant
Pitchoun                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Griddle cafe
Portos Bakery
Coffee house
Sidecar donuts
Groundwork's
Birreria San Marcos
Bombay Frankies
Lodge Bread
El Cochinito
Tacos El Venado
Barton G
Gracias madre
Ramen hood
Dirt Dog
Egg Slut
Los Feliz Square, Mexican Food
La flor de Yucatan Bakery
Lao Tao
Preux & Proper
Plan + Check
Maccheroni Republic
Shen Sin Gumi
77 Kentucky Chicken
Dumpling House
Sun Nong Dan
Larchmont Bungalow
Sqirl
Bulgogi Hut KBBQ
Hae Ha Heng
Isaan Station
The Oinkster
The Carving Board
Guisados'''.split("\n")


dessert_list = '''Jeni's Ice Cream
Compartes
California Donut
Cotton Hi
Drips & Swirls
Holy Roly
SomiSomi
Chocolate Chair
Sul & Beans
Boba Bear
Boba Story
Snow Monster
SnowLA Shavery
Carmela's
Cocobella Creamery
Night hawk
B sweet
Obica mozzarella bar
Trejos donuts
Magpies soft serve
Dominique ansel
Wanderlust Creamery
Peddler's Creamery
Gresescent
Salt & Straw
Little Damage
Toastea
Twinkle Brown Sugar
Honeymee'''.split("\n")

def getLoc(address):
    print('On address:' +address)
    geocode = gmaps.geocode(address)
    lat = geocode[0]['geometry']['location']['lat']
    long = geocode[0]['geometry']['location']['lng']
    return lat,long


gmaps = googlemaps.Client("AIzaSyADJgEX4dAErgPBkx0npekVAj07MLjAbb8")
# GoogleMapPlotter return Map object
# Pass the center latitude and
# center longitude
gmap1 = gmplot.GoogleMapPlotter(34.052234,
                                -118.243685, 13 )

latitude_list = []
longitude_list = []
for i in locations_list:
    lat,long = getLoc(i)
    latitude_list.append(lat)
    longitude_list.append(long)

gmap1.scatter( latitude_list, longitude_list, '#FF0000',
                              size = marker_size, marker = False )

latitude_list = []
longitude_list = []
for i in food_list:
    lat,long = getLoc(i)
    latitude_list.append(lat)
    longitude_list.append(long)


gmap1.scatter( latitude_list, longitude_list, '#0058e8', size = marker_size, marker = False )

latitude_list = []
longitude_list = []
for i in dessert_list:
    lat,long = getLoc(i)
    latitude_list.append(lat)
    longitude_list.append(long)


gmap1.scatter( latitude_list, longitude_list, '#06d314', size = marker_size, marker = False )

gmap1.scatter( [AirBNBLoc[0]], [AirBNBLoc[1]], '#d704e2', size = 350, marker = False )

# Pass the absolute path
gmap1.draw( os.getcwd()+"/index.html")

with open(os.getcwd()+"/index.html", "r") as f:
    a = f.read().replace("js?libraries","js?key=AIzaSyADJgEX4dAErgPBkx0npekVAj07MLjAbb8&libraries").replace("fillOpacity: 0.300000", "fillOpacity: 1.00000").replace("ROADMAP","ROADMAP,\nstyles: [{stylers: [{saturation: -100}]}]")

with open(os.getcwd()+"/index.html", "w") as f:
    f.write(a)
