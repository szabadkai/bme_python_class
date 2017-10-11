
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask("Atlas")
fh = open("sw_planets.csv", 'r')

planets={}
for line in fh:
    planet, region = line.strip().split(",")
    if not region in planets:
        planets[region] = [planet]
    else:
        planets[region].append(planet)



@app.route('/')
def welcome():
    return 'Hello Welcome to SWPlanets API'

@app.route('/planets')
def all_the_planets():
    planet_list = []
    for region in planets:
        planet_list += planets[region]
    return "<br>".join(planet_list)