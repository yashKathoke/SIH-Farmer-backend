from pydantic import BaseModel
from typing import Optional
from datetime import date

class WeatherRequest(BaseModel):
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    country: Optional[str] = None
    forecast_date: Optional[date] = None  # new field

class WeatherResponse(BaseModel):
    data: dict
