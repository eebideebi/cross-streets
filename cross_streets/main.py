from pydantic import BaseModel
from OSMPythonTools.overpass import Overpass
from .error_handling import Result, Ok, Err
from .street import Street
from .fuzzy_matching import find_most_similar_street, fetch_streets
from functools import cache
import usaddress 

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
        valid_streets = fetch_streets(self.searchArea,self.overpass)
        self.valid_streets = valid_streets.value if type(valid_streets) == Ok else None

    @cache
    def is_intersection(self, raw: str) -> bool:
        '''Determines whether or not the entered string is an Intersection\n
           Examples:
           * `Hennepin Ave S & West Lake Street` &rarr; `True`
           * `3048 Hennepin Ave` &rarr; `False`'''
           
        return usaddress.tag(raw)[1] == 'Intersection'
    
    def geocode(self, raw:str) -> Ok[Location]|Err:
        if not self.is_intersection(raw):
            return Err(error='This is not an intersection')

        # Get all permutations for the specified streets        
        tag = usaddress.tag(raw)[0]
        dict1 = {key:val for key,val in tag.items() if key.startswith('Street')}
        street1 = Street(dict1)
        dict2= {key[6:]:val for key,val in tag.items() if key.startswith('Second')}
        street2 = Street(dict2)
        
        # Attempt fuzzy matching:
        if self.valid_streets is None:
            return Err(error='Could not acquire street database')
        match1 = street1.get_best_match(self.valid_streets)
        match2 = street2.get_best_match(self.valid_streets)
                
        return self._geocode_clean_intersection(match1, match2)
            
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