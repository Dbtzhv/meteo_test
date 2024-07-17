from fastapi import HTTPException
from geopy import Nominatim


def get_city_coordinates(city: str) -> tuple[float, float]:
    geolocator = Nominatim(user_agent="meteo-test")

    location = geolocator.geocode(city)
    if not location:
        raise HTTPException(status_code=404, detail="City not found")

    latitude = location.latitude
    longitude = location.longitude

    return latitude, longitude