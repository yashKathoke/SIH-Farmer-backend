import requests

def get_weather_data(location=None, latitude=None, longitude=None):
    """
    Get weather conditions relevant to agriculture from Open-Meteo API.

    Parameters:
    - location: str (optional) e.g. "Pune, Maharashtra, India"
    - latitude: float (optional)
    - longitude: float (optional)

    Returns:
    - dict: Weather data (temperature, precipitation, soil moisture, etc.)
    """
    # 1. If location is provided, geocode to get lat/lon
    if location and (latitude is None or longitude is None):
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_params = {"name": location, "count": 1}
        geo_resp = requests.get(geo_url, params=geo_params)
        geo_resp.raise_for_status()
        geo_data = geo_resp.json()
        if "results" not in geo_data or not geo_data["results"]:
            raise ValueError(f"Could not find coordinates for location '{location}'")
        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]

    if latitude is None or longitude is None:
        raise ValueError("Please provide either location or latitude & longitude.")

    # 2. Call Open-Meteo API for weather
    weather_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,precipitation,soil_moisture_0_to_1cm,soil_temperature_0cm,evapotranspiration",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto"
    }
    resp = requests.get(weather_url, params=params)
    resp.raise_for_status()
    weather_data = resp.json()

    return weather_data
