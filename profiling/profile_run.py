from cross_streets import CrossStreets, Location, Result, Ok, Err 
import cProfile

def task(cs:CrossStreets):
    for input in [
        "Hennepin Avenue and South 1st Street",
        "East Lake Street & 11th Avenue South",
        "Northeast 26th Avenue and Northeast Jefferson Street",
    ]:
        print(cs.geocode(input, max_attempts=1))

cs = CrossStreets(
    searchArea = 'area(3600136712)',
    overpass_endpoint='https://maps.mail.ru/osm/tools/overpass/api/'
)

cProfile.run("task(cs)", "stats.dump")

# run this program to generate stats.dump
# run snakeviz stats.dump
# open url, ensure ends with: /snakeviz/stats.dump