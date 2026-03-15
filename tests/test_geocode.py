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