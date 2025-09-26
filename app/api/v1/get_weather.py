from fastapi import APIRouter, HTTPException
from app.schemas.weather import WeatherRequest, WeatherResponse
from app.services.llm_manager import llm_manager
from app.lib.get_weather_data import get_weather_data  # Assuming you place the function in a service file

router = APIRouter(prefix="/get-weather", tags=["get-weather"])

@router.post("/", response_model=WeatherResponse)
async def chat_endpoint(req: WeatherRequest):
    try:
        # Extract data from the request
        location = req.location
        latitude = req.latitude
        longitude = req.longitude

        # Get weather data
        weather_data = get_weather_data(location=location, latitude=latitude, longitude=longitude)

        return WeatherResponse(data=weather_data)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
