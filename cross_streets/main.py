from pydantic import BaseModel
from OSMPythonTools.overpass import Overpass

# --- Types ---

class Location(BaseModel):
    latitude: float
    longitude: float

# --- Main ---

class CrossStreets:
    def __init__(
        self,
        searchArea:str = 'area(3600136712)' # geocodeArea:Minneapolis
    ):
        self.overpass = Overpass()
        self.searchArea = searchArea

    def geocode(self, raw_intersection:str)->Location:
        street_1, street_2 = raw_intersection.split(' & ')
        return self._geocode_clean_intersection(street_1, street_2)
    
    def _geocode_clean_intersection(self, street_1:str, street_2):
        query = f'{self.searchArea}->.searchArea;way["highway"]["name"="Hennepin Avenue"](area.searchArea)->.w1;.searchArea;way["highway"]["name"="South 1st Street"](area.searchArea)->.w2; node(w.w1)(w.w2)->.intersection;(.intersection;);out body;'
        node = self.overpass.query(query).nodes()[0]
        return Location(latitude=node.lat(), longitude=node.lon())

if __name__ == "__main__":
    cs = CrossStreets()
    print(cs.geocode('Hennepin Avenue & South 1st Street'))