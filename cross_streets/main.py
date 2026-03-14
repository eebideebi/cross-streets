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

    def geocode(self, raw:str)->Location|None:
        street_1, street_2 = raw.split(' & ') if '&' in raw else raw.split(' and ')
        return self._geocode_clean_intersection(street_1, street_2)
    
    def _geocode_clean_intersection(self, street_1:str, street_2)->Location|None:
        query = f"""
            {self.searchArea}->.searchArea;
            way["highway"]["name"="{street_1}"](area.searchArea)->.w1;
            way["highway"]["name"="{street_2}"](area.searchArea)->.w2; 
            node(w.w1)(w.w2)->.intersection;
            (.intersection;);
            out body;
        """
        results = self.overpass.query(query)
        if results is None:
            return None
        else:
            node = results.nodes()[0]
            return Location(latitude=node.lat(), longitude=node.lon())

if __name__ == "__main__":
    cs = CrossStreets()
    print(cs.geocode('Hennepin Avenue & South 1st Street'))