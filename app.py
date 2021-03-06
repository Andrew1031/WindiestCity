from flask import Flask, request
from flask_cors import CORS
import sqlite3
from sqlite3 import Error
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/hello")
def findWindiest():
    conn = sqlite3.connect("./react-flask-app/www/citiesWindSpeed.db")
    c = conn.cursor()

    import requests
    import json

    cityAndWindSpeed = {}
    cities = ["Acton",
              "Adelanto",
              "Agua Dulce",
              "Alameda",
              "Alamo",
              "Albany",
              "Alhambra",
              "Aliso Viejo",
              "Alpine",
              "Alta Loma",
              "Altadena",
              "Alturas",
              "Amador City",
              "Anaheim",
              "Anderson",
              "Angels Camp",
              "Angelus Oaks",
              "Antelope",
              "Antioch",
              "Anza",
              "Apple Valley",
              "Applegate",
              "Aptos",
              "Arcadia",
              "Arcata",
              "Arleta",
              "Armona",
              "Arnold",
              "Arroyo Grande",
              "Atascadero",
              "Atwater",
              "Atwood",
              "Auberry",
              "Auburn",
              "Avalon",
              "Avery",
              "Azusa",
              "Bakersfield",
              "Bangor",
              "Banning",
              "Barstow",
              "Bay Point",
              "Bayside",
              "Bel Air",
              "Bell",
              "Bellflower",
              "Belmont",
              "Belvedere",
              "Ben Lomond",
              "Benicia",
              "Berkeley",
              "Berry Creek",
              "Beverly Hills",
              "Big Bear City",
              "Bishop",
              "Blue Jay",
              "Blythe",
              "Bolinas",
              "Bonita",
              "Bothell",
              "Boulder Creek",
              "Brea",
              "Brentwood",
              "Brisbane",
              "Buellton",
              "Burbank",
              "Burlingame",
              "Burlington",
              "Calabasas",
              "California City",
              "Calimesa",
              "Calistoga",
              "Camarillo",
              "Cambria",
              "Campbell",
              "Campo",
              "Canyon Country",
              "Capitola",
              "Cardiff",
              "Carlsbad",
              "Carmel",
              "Carmichael",
              "Carpinteria",
              "Carson",
              "Castaic",
              "Castro Valley",
              "Cathedral City",
              "Cayucos",
              "Ceres",
              "Cerritos",
              "Chatsworth",
              "Cherry Valley",
              "Chester",
              "Chico",
              "Chino",
              "Chula Vista",
              "Citrus Heights",
              "Claremont",
              "Clayton",
              "Cloverdale",
              "Clovis",
              "Coarsegold",
              "Colfax",
              "Coloma",
              "Colton",
              "Columbia",
              "Colusa",
              "Commerce",
              "Compton",
              "Concord",
              "Cordelia",
              "Corning",
              "Corona",
              "Coronado",
              "Corralitos",
              "Corte Madera",
              "Costa Mesa",
              "Cotati",
              "Coto de Caza",
              "Covina",
              "Crescent City",
              "Crestline",
              "Crockett",
              "Culver City",
              "Cupertino",
              "Cutten",
              "Cypress",
              "Daly City",
              "Dana Point",
              "Danville",
              "Davis",
              "Del Mar",
              "Desert Hot Springs",
              "Diamond Bar",
              "Dobbins",
              "Downey",
              "Duarte",
              "Dublin",
              "Durham",
              "Edwards",
              "El Cajon",
              "El Centro",
              "El Cerrito",
              "El Dorado",
              "El Granada",
              "Elk",
              "Elk Grove",
              "El Macero",
              "El Monte",
              "El Segundo",
              "Emeryville",
              "Encinitas",
              "Encino",
              "Escondido",
              "Etiwanda",
              "Etna",
              "Eureka",
              "Exeter",
              "Fairfax",
              "Fairfield",
              "Fair Oaks",
              "Fallbrook",
              "Felton",
              "Ferndale",
              "Fieldbrook",
              "Fillmore",
              "Flournoy",
              "Folsom",
              "Fontana",
              "Foothill Ranch",
              "Foresthill",
              "Forest Ranch",
              "Fortuna",
              "Foster City",
              "Fountain Valley",
              "Frazier Park",
              "Freedom",
              "Fremont",
              "Fresno",
              "Frogtown",
              "Fullerton",
              "Galt",
              "Garberville",
              "Gardena",
              "Garden Grove",
              "Gilroy",
              "Glendale",
              "Glendora",
              "Glen Ellen",
              "Glenn",
              "Goleta",
              "Grand Terrace",
              "Grass Valley",
              "Greenbrae",
              "Groveland",
              "Gualala",
              "Guerneville",
              "Hacienda Heights",
              "Half Moon Bay",
              "Hanford",
              "Harbor City",
              "Hawthorne",
              "Hayfork",
              "Hayward",
              "Healdsburg",
              "Hemet",
              "Hercules",
              "Hesperia",
              "Highland",
              "Hinkley",
              "Hollister",
              "Hollywood",
              "Homeland",
              "Honcut",
              "Humboldt",
              "Idyllwild",
              "Imperial",
              "Independence",
              "Indian Wells",
              "Indio",
              "Inglewood",
              "Inverness",
              "Ione",
              "Irvine",
              "Irwindale",
              "Isla Vista",
              "Isleton",
              "Jackson",
              "Jamestown",
              "Jamul",
              "Jenner",
              "Joshua Tree",
              "Julian",
              "Kelseyville",
              "Kensington",
              "Kentfield",
              "Kenwood",
              "King City",
              "Klamath",
              "La Crescenta",
              "La Habra",
              "La Honda",
              "La Jolla",
              "La Mirada",
              "La Quinta",
              "La Verne",
              "Ladera Ranch",
              "Lafayette",
              "Laguna Niguel",
              "Lakeport",
              "Lakeside",
              "Lakeview Terrace",
              "Lakewood",
              "Lamont",
              "Lancaster",
              "Larkspur",
              "Lathrop",
              "Lawndale",
              "Lemon Grove",
              "Lemoore",
              "Lewiston",
              "Littlerock",
              "Livermore",
              "Llano",
              "Lodi",
              "Loleta",
              "Lomita",
              "Lompoc",
              "Long Beach",
              "Loomis",
              "Los Alamitos",
              "Los Altos",
              "Los Angeles",
              "Los Banos",
              "Los Gatos",
              "Los Osos",
              "Lotus",
              "Lower Lake",
              "Magalia",
              "Malibu",
              "Mammoth Lakes",
              "Manhattan Beach",
              "Manteca",
              "Manton",
              "Marina",
              "Mariposa",
              "Martinez",
              "Marysville",
              "McKinleyville",
              "Meadow Vista",
              "Mendocino",
              "Menlo Park",
              "Merced",
              "Middletown",
              "Midway City",
              "Millbrae",
              "Mill Valley",
              "Milpitas",
              "Mira Loma",
              "Mission Hills",
              "Mission Viejo",
              "Modesto",
              "Mojave",
              "Monrovia",
              "Montague",
              "Montara",
              "Montclair",
              "Montecito",
              "Monterey",
              "Monte Sereno",
              "Montrose",
              "Moorpark",
              "Moraga",
              "Moreno Valley",
              "Morgan Hill",
              "Morro Bay",
              "Mountain Ranch",
              "Mountain View",
              "Murrieta",
              "Napa",
              "National City",
              "Nevada City",
              "New Almaden",
              "Newark",
              "Newhall",
              "Newport",
              "Nicasio",
              "Nice",
              "Nipomo",
              "Norco",
              "North Highlands",
              "Northridge",
              "Norwalk",
              "Novato",
              "Oakdale",
              "Oakhurst",
              "Oakland",
              "Oakley",
              "Oak Park",
              "Occidental",
              "Oceanside",
              "Ojai",
              "Ontario",
              "Orange",
              "Orangevale",
              "Oregon House",
              "Orinda",
              "Oroville",
              "Oxnard",
              "Pacheco",
              "Pacifica",
              "Pacoima",
              "Palermo",
              "Palmdale",
              "Palm Desert",
              "Palm Springs",
              "Palo Alto",
              "Palo Cedro",
              "Palos Verdes",
              "Paradise",
              "Paramount",
              "Pasadena",
              "Paso Robles",
              "Patterson",
              "Perris",
              "Petaluma",
              "Pico Rivera",
              "Piedmont",
              "Pinole",
              "Pioneer",
              "Pittsburg",
              "Placentia",
              "Placerville",
              "Playa del Rey",
              "Pleasanton",
              "Plymouth",
              "Pomona",
              "Poway",
              "Prather",
              "Quincy",
              "Ramona",
              "Rancho Bernardo",
              "Rancho Cordova",
              "Rancho Cucamonga",
              "Rancho Dominguez",
              "Rancho Mirage",
              "Rancho Palos Verdes",
              "Rancho Santa Fe",
              "Rancho Santa Margarita",
              "Red Bluff",
              "Redding",
              "Redlands",
              "Redway",
              "Redwood City",
              "Rescue",
              "Reseda",
              "Rialto",
              "Richmond",
              "Ridgecrest",
              "Ripon",
              "Riverbank",
              "Riverside",
              "Rocklin",
              "Rosamond",
              "Rosemead",
              "Roseville",
              "Ross",
              "Sacramento",
              "Salida",
              "Salinas",
              "Salton City",
              "San Anselmo",
              "San Bernardino",
              "San Bruno",
              "San Carlos",
              "San Clemente",
              "San Diego",
              "San Dimas",
              "San Fernando",
              "San Francisco",
              "San Gabriel",
              "San Gregorio",
              "San Jacinto",
              "San Jose",
              "San Juan Bautista",
              "San Juan Capistrano",
              "San Leandro",
              "San Lorenzo",
              "San Luis Obispo",
              "San Marcos",
              "San Marino",
              "San Martin",
              "San Mateo",
              "San Pablo",
              "San Pedro",
              "San Rafael",
              "San Ramon",
              "San Ysidro",
              "Sanger",
              "Santa Ana",
              "Santa Barbara",
              "Santa Clara",
              "Santa Clarita",
              "Santa Cruz",
              "Santa Fe Springs",
              "Santa Margarita",
              "Santa Maria",
              "Santa Monica",
              "Santa Paula",
              "Santa Rosa",
              "Santa Ynez",
              "Santee",
              "Saratoga",
              "Saugus",
              "Sausalito",
              "Scotia",
              "Sea Ranch",
              "Seaside",
              "Sebastopol",
              "Shafter",
              "Sherman",
              "Sherman Oaks",
              "Sierra Madre",
              "Signal Hill",
              "Silverado",
              "Simi Valley",
              "Skyforest",
              "Soledad",
              "Solvang",
              "Somerset",
              "Sonoma",
              "Sonora",
              "Soquel",
              "South Gate",
              "Spring Valley",
              "Springville",
              "Stanford",
              "Stanislaus",
              "Stockton",
              "Suisun",
              "Summerland",
              "Sun City",
              "Sunland",
              "Sunnyvale",
              "Sunol",
              "Sun Valley",
              "Surfside",
              "Sylmar",
              "Taft",
              "Tahoe City",
              "Tarzana",
              "Tehachapi",
              "Temecula",
              "Temple City",
              "Templeton",
              "Thousand Oaks",
              "Three Rivers",
              "Tiburon",
              "Tierrasanta",
              "Topanga",
              "Torrance",
              "Tracy",
              "Trinidad",
              "Truckee",
              "Tulare",
              "Turlock",
              "Tustin",
              "Twain Harte",
              "Twentynine Palms",
              "Ukiah",
              "Union City",
              "Universal City",
              "Upland",
              "Vacaville",
              "Valencia",
              "Vallejo",
              "Valley Center",
              "Valley Glen",
              "Van Nuys",
              "Venice",
              "Ventura",
              "Vernalis",
              "Victor",
              "Victorville",
              "Vineburg",
              "Visalia",
              "Vista",
              "Walnut",
              "Walnut Creek",
              "Watsonville",
              "Weaverville",
              "Weed",
              "West Covina",
              "West Hills",
              "West Hollywood",
              "Westlake",
              "West Lancaster",
              "Westminster",
              "Westwood",
              "Whitmore",
              "Whittier",
              "Wildomar",
              "Willits",
              "Wilmington",
              "Windsor",
              "Winnetka",
              "Woodland",
              "Woodside",
              "Yorba Linda",
              "Yountville",
              "Yreka",
              "Yuba City",
              "Yucaipa",
              "Yucca Valley"]

    # Creates SQLite database table listing the cities as columns, and date/time as rows
    createTable = "CREATE TABLE if not exists windSpeeds (Date_Time text, Windiest_City_And_Speed text, "
    for city in cities:
        if ' ' in city:
            city = city.replace(' ', '_')
        createTable = createTable + city + " text, "

    size = len(createTable)
    createTable = createTable[:size-2]
    createTable = createTable + ")"
    c.execute(createTable)

    # traverses through each city and stores the wind speed
    dateTimeObj = datetime.now()
    insertCity = ""
    insertCities = ""
    insertSpeed = ""
    insertValues = ""
    for city in cities:
        insertCity = city
        if ' ' in insertCity:
            insertCity = insertCity.replace(' ', '_')
        apiUrl = "http://api.openweathermap.org/data/2.5/weather?q=" + city + \
                 "&appid=e9883e4a2bd0bf92187695b6788a0da8"
        response = requests.get(apiUrl)
        windspeed = response.json()['wind']['speed']
        cityAndWindSpeed[city] = windspeed
        insertCities = insertCities + ", " + insertCity
        insertSpeed = str(windspeed)
        insertValues = insertValues + ", " + insertSpeed

    #prints out the windiest city
    windiestCity = max(cityAndWindSpeed, key=cityAndWindSpeed.get)

    #inserts all the data into sqlite table
    dateAndTime = str(dateTimeObj)
    insertCities = "Date_Time, Windiest_City_And_Speed" + insertCities
    insertCommand = "INSERT INTO windSpeeds(" + insertCities + ")" + " VALUES ("+ \
                    "'" + str(dateAndTime) + "'" + ", " + "'" + str(windiestCity) + \
                    " " + str(cityAndWindSpeed[windiestCity]) + "'" + insertValues + ")"
    c.execute(insertCommand)
    conn.commit()
    conn.close()

    return {'result': windiestCity + " " + str(cityAndWindSpeed[windiestCity])}
