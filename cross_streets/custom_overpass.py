from .error_handling import Result, Ok, Err
from datetime import datetime
from urllib.parse import urlencode
from json import loads
import requests
from functools import cache

class Element:
    type: str
    id: int
    lat: float|None
    long: float|None
    tags: dict[str,str]|None
    
    def __init__(self, element: dict):
        self.id = element['id']
        self.type = element['type']
        if lat:=element.get('lat'): self.lat = float(lat)
        if long:=element.get('lon'): self.long = float(long)
        if tags:=element.get('tags'): self.tags = tags 
        
    
    def __str__(self):
        out = "Element"
        if self.id: out += f'\n\tid\t{self.id}'
        if self.type: out += f'\n\ttype\t{self.type}'
        if self.lat: out += f'\n\tlat\t{self.lat}'
        if self.long: out += f'\n\tlong\t{self.long}'
        if self.tags: out += f'\n\ttags:\n\t\t{'\n\t\t'.join([f'"{k}": "{v}"' for k,v in self.tags.items()])}'
        return out
    
    def tag(self, key: str) -> str|None:
        if self.tags is None:
            return None
        return self.tags.get(key)
    
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Overpass:    
    search_area: str
    endpoints: list[str]
    verbose: bool
    
    def __init__(
        self,
        search_area: str = 'area(3600136712)', # geocodeArea:Minneapolis
        endpoints: list[str] = ['https://overpass-api.de/api/','https://maps.mail.ru/osm/tools/overpass/api/'],
        verbose: bool = False
    ):
        self.verbose = verbose
        self.search_area = search_area 
        if len(endpoints) == 0:
            raise RuntimeError(bcolors.FAIL + '[ERROR] Overpass: Cannot initialize with no endpoints' + bcolors.ENDC)
        elif len(endpoints) < 2: 
            self.print(bcolors.WARNING + '[WARNING] Overpass: It is unadvisable to only specify one endpoint with no fallbacks!' + bcolors.ENDC)
        self.endpoints = list(map(lambda x: x[:-1] if x.endswith('/') else x, endpoints))   
        
    def print(self, *args):
        if self.verbose:
            print(*args)
    
    @cache
    def fetch_streets(self)->Result[set[str]]:
        query = f"""
            {self.search_area}->.searchArea;
            way["highway"]["name"](area.searchArea);
            out tags;
        """

        results = self.query(query)
        if isinstance(results, Err):
            return Err(error='Error connecting to overpass server')
        elif not (ways := results.value):
            return Err(error='No Streets found')
        else:
            ways = self.ways(query)
            if isinstance(ways, Err):
                return ways
            return Ok(value=set(filter(None, [way.tag('name') for way in ways.value])))
    
    def validate(self):
        self.print(bcolors.HEADER + 'Validating endpoints' + bcolors.ENDC)
        for endpoint in self.endpoints:
            query = endpoint + '/interpreter/?' + urlencode({'data': f'way["name"="{datetime.now().isoformat()}"]; out body;'})
            self.print(bcolors.BOLD + '\tValidating',endpoint,'with the following query:' + bcolors.ENDC)
            self.print('\t\t'+ query)
            try:
                result = self.query(f'way["name"="{datetime.now().isoformat()}"]; out body;', endpoint)
                assert isinstance(result, Ok)
                self.print(bcolors.OKGREEN + '\t\tSuccess!' + bcolors.ENDC)
            except:
                err = f'Endpoint ({endpoint}) is not responding or invalid.'
                raise RuntimeError(err)
            
    @cache
    def query(self, query_str: str, endpoint: str|None = None) -> Result[dict]:
        endpoints = self.endpoints if endpoint is None else [endpoint]
        query_str = f'{urlencode({'data': f'[out:json];{self.search_area}->.searchArea;{query_str}'})}'
                
        for endpoint in endpoints:
            query = f'{endpoint}/interpreter/?{query_str}'
            try:
                response = requests.get(query)
                # Allow backup endpoints to pick up slack:
                if not response.ok:
                    continue
                return Ok(value=loads(response.text))
            except:
                self.print(bcolors.WARNING + f'[WARNING] Overpass: endpoint unreachable: {query}' + bcolors.ENDC)
                
        return Err(error=f"All endpoints failed. Attempted: {', '.join(endpoints)}")
    
    @cache
    def elements(self, query_str: str, endpoint: str|None = None) -> Result[list[Element]]:
        result = self.query(query_str, endpoint)
        if isinstance(result, Err):
            return result
        return Ok(value=list(map(lambda x: Element(x), result.value['elements'])))
    
    @cache
    def nodes(self, query_str: str, endpoint: str|None = None):
        result = self.query(query_str, endpoint)
        if isinstance(result, Err):
            return result
        
        elements = list(map(lambda e: Element(e), result.value['elements']))
        return Ok(value=list(filter(lambda n: n.type == 'node', elements)))
    
    @cache
    def ways(self, query_str: str, endpoint: str|None = None):
        result = self.query(query_str, endpoint)
        if isinstance(result, Err):
            return result
        elements = list(map(lambda e: Element(e), result.value['elements']))
        return Ok(value=list(filter(lambda n: n.type == 'way', elements)))
        
if __name__ == '__main__':
    overpass = Overpass('area(3600136712)',['https://overpass-api.de/api/'],True)
    overpass.validate()
    
    search_area = 'area(3600136712)'
    street_1 = 'Hennepin Avenue'
    street_2 = 'South 1st Street'
    
    query = f"""
            {search_area}->.searchArea;
            way["highway"]["name"="{street_1}"](area.searchArea)->.w1;
            way["highway"]["name"="{street_2}"](area.searchArea)->.w2; 
            node(w.w1)(w.w2)->.intersection;
            (.intersection;);
            out body;
        """
        
    # elements = overpass.elements(query)
    # assert isinstance(elements, Ok)
    # for e in elements.value:
    #     self.print(e)
        
    # nodes = overpass.nodes(query)
    # assert isinstance(nodes, Ok)
    # for n in nodes.value:
    #     self.print(n)
    
    streets = overpass.fetch_streets()
