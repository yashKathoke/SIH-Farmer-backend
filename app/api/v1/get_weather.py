from fastapi import APIRouter, HTTPException
from app.schemas.weather import WeatherRequest, WeatherResponse
from app.lib.get_weather_data import get_weather_data  # Assuming you place the function in a service file

router = APIRouter(prefix="/get-weather", tags=["get-weather"])

@router.post("/", response_model=WeatherResponse)
async def get_weather_endpoint(req: WeatherRequest):
    try:
        # Extract data from the request
        location = req.location
        latitude = req.latitude
        longitude = req.longitude
        country = getattr(req, "country", None)  # optional field
        forecast_date = getattr(req, "forecast_date", None)  # optional field

        # Get weather data
        weather_data = get_weather_data(
            location=location,
            latitude=latitude,
            longitude=longitude,
            country=country,
            forecast_date=forecast_date
        )

        return WeatherResponse(data=weather_data)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
