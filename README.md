# cross_streets
Python Library that translates cross streets into Overpass/Nominatim queries 

# Usage

## Install Package

```bash
pip install CrossStreets 
```

## Most basic example

```python
>>> import cross_streets
>>> cs = cross_streets.CrossStreets()
>>> cs.geocode('Hennepin Avenue & South 1st Street')
Ok(value=Location(latitude=44.9837435, longitude=-93.2665678))
```

# Building from source
1. Clone this repository
2. Install `requirements.txt`
3. Run `python setup.py sdist bdist_wheel`
4. `pip uninstall cross-streets`
5. `pip install dist/%.whl file created by step three%`
`
# Data sources:
* [Wikipedia Street Types](https://en.wikipedia.org/wiki/Street_suffix)

# TODO List
- [ ] permutation from written numbers to digits and visa versa
- [ ] optionally include cities in overpass call
- [ ] add fallback endpoint