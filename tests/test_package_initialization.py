import cross_streets as cs

# import pytest

def test_intialization():
    streets = cs.CrossStreets()
    assert type(streets.geocode('test')) == cs.main.Location
