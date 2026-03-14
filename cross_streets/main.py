from pydantic import BaseModel

class Location(BaseModel):
    latitude: float
    longitude: float

class CrossStreets:
    def __init__(self):
        print("running init")
    def geocode(self, raw_intersection:str)->Location:
        return Location(latitude=1, longitude=1)

if __name__ == "__main__":
    cs = CrossStreets()
    print(cs.geocode('test'))