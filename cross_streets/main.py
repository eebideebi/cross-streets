from pydantic import BaseModel
from OSMPythonTools.overpass import Overpass
from error_handeling import Result, Ok, Err 

# --- Types ---

class Location(BaseModel):
    latitude: float
    longitude: float

# --- Main ---

class CrossStreets:
    def __init__(
        self,
        searchArea:str = 'area(3600136712)', # geocodeArea:Minneapolis
        overpass_endpoint:str|None = None
    ):
        self.overpass = Overpass(endpoint=overpass_endpoint) if overpass_endpoint else Overpass()
        self.searchArea = searchArea

    def geocode(self, raw:str)->Result[Location]:
        street_1, street_2 = raw.split(' & ') if '&' in raw else raw.split(' and ')
        return self._geocode_clean_intersection(street_1, street_2)
    
    def _geocode_clean_intersection(self, street_1:str, street_2)->Result[Location]:
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
            return Err(error='Error connecting to overpass server')
        if not results.nodes():
            return Err(error='No intersection found')
        else:
            # TODO handle if multiple nodes are found
            node = results.nodes()[0]
            return Ok(value=Location(latitude=node.lat(), longitude=node.lon()))

if __name__ == "__main__":
    cs = CrossStreets()
    print(cs.geocode('Hennepin Avenue & South 1st Street'))
    print(cs.geocode('Avenue Hennepin & South 1st Street'))