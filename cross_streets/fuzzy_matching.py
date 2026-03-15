from OSMPythonTools.overpass import Overpass
from .error_handling import Result, Ok, Err
import rapidfuzz

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

def find_most_similar_street(valid_streets:set[str], search_term:str)->Result[dict[str,str|float]]:
    extraction = rapidfuzz.process.extractOne(
        search_term, 
        valid_streets, 
        scorer=rapidfuzz.fuzz.ratio
    )
    if extraction is None:
        return Err(error=f'No street similar to {search_term}')
    best_match, score, _ = extraction
    # print(f"Best match found: '{best_match}'")
    # print(f"Similarity score (0-100): {score}")
    return Ok(value={'match': str(best_match), 'score': score})

# TODO cache_street
# TODO update_cache
if __name__ == "__main__":
    streets:Result = fetch_streets('area(3600136712)', Overpass())
    if isinstance(streets, Ok):
        search_term = 'wilderr St'
        print(f'closes match to {search_term}:')
        print(find_most_similar_street(valid_streets=streets.value, search_term=search_term))