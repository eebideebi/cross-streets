from pydantic import BaseModel

class Location(BaseModel):
    latitude: float
    longitude: float

class CrossStreets:
    def __init__():
        print(running init)
    def geocode(raw_intersection:str)->Location:
        return Location(1, 1)

if __name__ == "__main__":
    cs = CrossStreets()
    print(geocode('test'))