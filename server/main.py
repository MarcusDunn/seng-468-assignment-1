import requests
from fastapi import FastAPI
from pydantic import BaseModel
from requests import Response

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
    resp: Response = requests.get("https://api.open-meteo.com/v1/forecast", params=params, allow_redirects=True)
    json: Forcast = resp.json()
    return json


class HealthCheck(BaseModel):
    status: str


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}
