from cross_streets import CrossStreets, Location, Result, Ok, Err 
import pytest

#  --- geocode_clean_intersection ---

@pytest.mark.parametrize(
    "street_1, street_2, lat, long",
    [
        ("Hennepin Avenue", "South 1st Street", 44.9837435, -93.2665678),
        ("East Lake Street", "11th Avenue South", 44.9483621, -93.2588673),
        ("Northeast 26th Avenue", "Northeast Jefferson Street", 45.0149699, -93.2555096),
    ]
)
def test_geocode_clean_intersection_correct(street_1, street_2, lat, long):
    cs = CrossStreets(
        searchArea = 'area(3600136712)',
        overpass_endpoint='https://maps.mail.ru/osm/tools/overpass/api/'
    )
    result = cs._geocode_clean_intersection(street_1, street_2)
    print(result)
    assert isinstance(result, Ok)
    assert result.value[0] == Location(latitude=lat, longitude=long)

def test_geocode_clean_intersection_invalid_overpass_endpoint():
    with pytest.raises(RuntimeError):
        cs = CrossStreets(overpass_endpoint="no endpoint")
        
        
@pytest.mark.parametrize(
    "street_1, street_2, lat, long",
    [
        ("Hennepin Avenue", "South 1st Street", 44.9837435, -93.2665678),
        ("East Lake Street", "11th Avenue South", 44.9483621, -93.2588673),
        ("Northeast 26th Avenue", "Northeast Jefferson Street", 45.0149699, -93.2555096),
    ]
)
def test_basic_examples(street_1, street_2, lat, long):
    '''These basic examples should have perfect matches in the DB.
       As such, they must succeed on the first attempt.'''
    
    input = f'{street_1} and {street_2}'
    streets = CrossStreets()
    result = streets.geocode(input, max_attempts=1)
    assert isinstance(result, Ok)
    assert result.value[0].latitude == lat
    assert result.value[0].longitude == long
    
@pytest.mark.parametrize(
    'street_1, street_2, lat, long',
    [
        ('S Hennepin Ave','South 1st St', 44.9837435, -93.2665678)
    ]
)
def test_mistyped_query(street_1, street_2, lat, long):
    '''The input string a street that doesn't exist,
        but which closely matches a real street 
        ('S Hennepin Ave' vs. 'Hennepin Avenue').\n
        `geocode()` should still successfully find a match'''
        
    input = f'{street_1} & {street_2}'
    streets = CrossStreets()
    result = streets.geocode(input)
    print(result)
    assert isinstance(result,Ok)
    assert result.value[0].latitude == lat
    assert result.value[0].longitude == long