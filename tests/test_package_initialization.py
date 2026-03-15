import cross_streets

# import pytest

def test_intialization():
    streets = cross_streets.CrossStreets()
    result = streets.geocode('S Hennepin Ave & South 1st St')
    assert isinstance(result,cross_streets.main.Ok)
