fh = open("sw_planets.csv", 'r')

planets={}
# build up a dictionary where the key is the name of the region
# and the corresponding value is a list of planets in the region
# plus points for a PR with proper csv parsing. :)
for line in fh:
    planet, region = line.strip().split(",")
    if not region in planets:
        planets[region] = [planet]
    else:
        planets[region].append(planet)


max_len=0
biggest_region = ""
for region in planets:
    if len(planets[region]) >max_len:
        max_len = len(planets[region])
        biggest_region = region


print("bigges region is {region} with {len} planets"
.format(region=biggest_region, len=max_len))