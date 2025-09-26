from pydantic import BaseModel

class WeatherRequest(BaseModel):
    location: str = None
    latitude: float = None
    longitude: float = None

class WeatherResponse(BaseModel):
    data: dict
           