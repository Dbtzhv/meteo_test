import aiohttp

from fastapi import APIRouter, status
from fastapi import HTTPException, Request, Query
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from services import get_city_coordinates


weather_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@weather_router.get("/", status_code=status.HTTP_200_OK, summary="Weather page", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("/weather.html", {"request": request, "weather": None})


@weather_router.get("/weather", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = Query(..., min_length=1)):
    latitude, longitude = get_city_coordinates(city)

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,apparent_temperature"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.open-meteo.com/v1/forecast", params=params) as resp:
            if resp.status == 200:
                data = await resp.json()
                weather_data = {
                    "request": request,
                    "city": city,
                    "weather": data
                }
                return templates.TemplateResponse("weather.html", weather_data)
            else:
                raise HTTPException(status_code=resp.status, detail="Error fetching weather data")

