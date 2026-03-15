import cross_streets as cs

# import pytest

def test_intialization():
    streets = cs.CrossStreets()
    assert type(streets.geocode('S Hennepin Ave & South 1st St')) == cs.main.Location
