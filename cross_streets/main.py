from pydantic import BaseModel
# from OSMPythonTools.overpass import Overpass
from .custom_overpass import Overpass, Element
from .error_handling import Result, Ok, Err
from .street import Street
from datetime import datetime
from functools import cache
import usaddress 

# --- Helper ---

def validate_overpass_endpoint(overpass:Overpass):
    try:
        assert overpass.query(f'way["name"="{datetime.now().isoformat()}"]; out body;') is not None
    except:
        raise RuntimeError("Overpass endpoint is not responding or invalid.")


# --- Types ---

class Location(BaseModel):
    latitude: float
    longitude: float

# --- Main ---

class CrossStreets:
    def __init__(
        self,
        search_area: str = 'area(3600136712)', # geocodeArea:Minneapolis
        endpoints: list[str] = ['https://overpass-api.de/api/','https://maps.mail.ru/osm/tools/overpass/api/']
    ):
        self.overpass = Overpass(search_area, endpoints)
        self.overpass.validate()
        
        self.search_area = search_area
        valid_streets = self.overpass.fetch_streets()
        self.valid_streets = valid_streets.value if isinstance(valid_streets, Ok) else None

    @cache
    def is_intersection(self, raw: str) -> bool:
        '''Determines whether or not the entered string is an Intersection\n
           Examples:
           * `Hennepin Ave S & West Lake Street` &rarr; `True`
           * `3048 Hennepin Ave` &rarr; `False`'''
           
        return usaddress.tag(raw)[1] == 'Intersection'
    
    def geocode(self, raw:str, max_attempts: int = 3) -> Ok[list[Location]]|Err:
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
        candidates1 = street1.get_best_matches(self.valid_streets)
        candidates2 = street2.get_best_matches(self.valid_streets)
        # Combine streets to find best composite score:
        matches: list[dict[str,str|float]] = []
        for c1 in candidates1:
            for c2 in candidates2:
                if c1['match'] == c2['match']: # streets can't be 100% identical
                    continue
                matches.append(
                    {
                        'street1': c1['match'],
                        'street2': c2['match'],
                        'score': float(c1['score']) + float(c2['score'])
                    }
                )
        matches.sort(reverse=True, key=lambda x: x['score'])
        # Try to find a valid geodocing:
        for match in matches[:max_attempts]:
            result = self._geocode_clean_intersection(str(match['street1']), str(match['street2']))
            # Output first valid match
            if isinstance(result,Ok):
                return result
            
        return Err(error='No matching intersection found :(')
                    
    def _geocode_clean_intersection(self, street_1:str, street_2: str)->Result[list[Location]]:
        # TODO: Include city/zip in query
        query = f"""
            {self.search_area}->.searchArea;
            way["highway"]["name"="{street_1}"](area.searchArea)->.w1;
            way["highway"]["name"="{street_2}"](area.searchArea)->.w2; 
            node(w.w1)(w.w2)->.intersection;
            (.intersection;);
            out body;
        """
        
        results = self.overpass.nodes(query)
        if isinstance(results, Err):
            return results
        
        nodes = list(filter(lambda x: x.lat and x.long, results.value))
        return Ok(value=[Location(latitude=node.lat or 0, longitude=node.long or 0) for node in nodes])

if __name__ == "__main__":
    cs = CrossStreets()
    print(cs.geocode('Hennepin Avenue & South 1st Street'))
    print(cs.geocode('Avenue Hennepin & South 1st Street'))