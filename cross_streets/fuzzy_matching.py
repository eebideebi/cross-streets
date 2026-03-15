from OSMPythonTools.overpass import Overpass
from .error_handling import Result, Ok, Err
import rapidfuzz
from collections import Counter


def fetch_streets(searchArea, overpass:Overpass)->Result[set[str]]:
    query = f"""
        {searchArea}->.searchArea;
        way["highway"]["name"](area.searchArea);
        out tags;
    """
    results = overpass.query(query)
    if results is None:
        return Err(error='Error connecting to overpass server')
    if not (ways := results.elements()):
        return Err(error='No Streets found')
    else:
        return Ok(value=set(way.tag('name') for way in ways))

def digits_in_string(input_string)->Counter:
    return Counter(char for char in input_string if char.isdigit() )

def find_most_similar_street(valid_streets:set[str], search_term:str)->Result[dict[str,str|float]]:
    search_term_digits = digits_in_string(search_term)

    extraction = rapidfuzz.process.extract(
        search_term, 
        valid_streets, 
        scorer=rapidfuzz.fuzz.ratio,
        limit = 15
    )

    if len(extraction) == 0:
        return Err(error=f'No street similar to {search_term}')
    
    for best_match, score, _ in extraction:
        if digits_in_string(best_match) == search_term_digits:
            return Ok(value={'match': str(best_match), 'score': score})
        
    return Err(error=f'No street similar to {search_term} with the same digits')

# TODO cache_street
# TODO update_cache occasionally
if __name__ == "__main__":
    streets:Result = fetch_streets('area(3600136712)', Overpass())
    if isinstance(streets, Ok):
        search_term = 'South 17th Street'
        print(f'closes match to {search_term}:')
        print(find_most_similar_street(valid_streets=streets.value, search_term=search_term))