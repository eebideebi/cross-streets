import cross_streets

# import pytest

def test_initialization():
    assert isinstance(cross_streets.CrossStreets(), cross_streets.CrossStreets)

def test_init_valid_streets():
    streets = cross_streets.CrossStreets()
    assert isinstance(streets.valid_streets, set)