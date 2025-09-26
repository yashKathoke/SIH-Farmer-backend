import requests
from datetime import date
from typing import Optional

def get_weather_data(
    location: Optional[str] = None,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
    country: Optional[str] = None,
    forecast_date: Optional[date] = None
):
    """
    Get weather conditions relevant to agriculture from Open-Meteo API.

    Parameters:
    - location: str (optional) e.g. "Pune, Maharashtra, India" or "411001"
    - latitude: float (optional)
    - longitude: float (optional)
    - country: str (optional) ISO country code
    - forecast_date: date (optional) if you want data for a specific day

    Returns:
    - dict: Weather data
    """
    # 1. Geocode if needed
    if location and (latitude is None or longitude is None):
        clean_query = location.split(",")[0].strip()
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_params = {"name": clean_query, "count": 1}
        if country:
            geo_params["country"] = country
        geo_resp = requests.get(geo_url, params=geo_params)
        geo_resp.raise_for_status()
        geo_data = geo_resp.json()
        if "results" not in geo_data or not geo_data["results"]:
            raise ValueError(f"Could not find coordinates for location '{location}'")
        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]

    if latitude is None or longitude is None:
        raise ValueError("Please provide either location or latitude & longitude.")

    # 2. Weather API parameters
    weather_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,precipitation,soil_moisture_0_to_1cm,soil_temperature_0cm,evapotranspiration",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto"
    }

    # add date range if provided
    if forecast_date:
        # if you want exactly that date’s forecast, set both start and end to forecast_date
        d_str = forecast_date.strftime("%Y-%m-%d")
        params["start_date"] = d_str
        params["end_date"] = d_str

    resp = requests.get(weather_url, params=params)
    resp.raise_for_status()
    return resp.json()


def get_weather_by_location(location: str):
    """
    Get agricultural weather data from Open-Meteo using a location name or pincode.
    Handles city/state/country strings gracefully.
    """
    # Clean up input (take first token before comma if needed)
    clean_query = location.split(",")[0].strip()

    # Geocode
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {"name": clean_query, "count": 1}
    geo_resp = requests.get(geo_url, params=geo_params)
    geo_resp.raise_for_status()
    geo_data = geo_resp.json()

    if "results" not in geo_data or not geo_data["results"]:
        raise ValueError(f"Could not find coordinates for location '{location}'")

    place = geo_data["results"][0]
    lat = place["latitude"]
    lon = place["longitude"]

    # Weather API
    weather_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation,soil_moisture_0_to_1cm,soil_temperature_0cm,evapotranspiration",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto"
    }
    resp = requests.get(weather_url, params=params)
    resp.raise_for_status()
    return resp.json()
