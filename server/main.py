import logging

import requests
from fastapi import FastAPI
from pydantic import BaseModel
from requests import Response

logger = logging.getLogger()

app = FastAPI()


class Weather(BaseModel):
    temperature: float
    windspeed: float
    winddirection: float
    weathercode: int
    time: str


class Forcast(BaseModel):
    latitude: float
    longitude: float
    generationtime_ms: float
    utc_offset_seconds: int
    timezone: str
    timezone_abbreviation: str
    elevation: float
    current_weather: Weather


@app.get("/forcast/")
def root(lat: float, lng: float) -> Forcast:
    params = {"latitude": lat, "longitude": lng, "current_weather": True}
    logger.info(f"requesting forcast for {lat}, {lng}")
    resp: Response = requests.get("https://api.open-meteo.com/v1/forecast", params=params, allow_redirects=True)
    logger.info(f"response received")
    json: Forcast = resp.json()
    return json
