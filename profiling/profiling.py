from cross_streets import CrossStreets
import profile

streets = CrossStreets()

def main():
    for _ in range(100):
        streets.geocode('Hennepin Avenue & West Lake St')
    

print('starting profile...')
profile.run('main()', sort='tottime')
print('profiling complete')