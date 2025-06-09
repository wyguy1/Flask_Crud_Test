from flask import Blueprint, render_template
import requests

weather_bp = Blueprint('weather_bp', __name__)

@weather_bp.route("/weather_current", methods=["GET", "POST"])
def weather_current():
    temp,wnd,windDir = weatherBigMain(36.87, -95.11)  # Welch, OK
    return render_template("weather-current.html", weather=temp, windSpeed=round(wnd), windDirection=windDir)

def fTocConversion(x):
    temp = (x * 1.8) + 32
    return temp

def wndSpeedtoMPH(x):

    wndMPH = x * .621371
    return wndMPH

def wndDir(x):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    index = round(x / 45) % 8
    return directions[index]


def weatherBigMain(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    current = data.get("current_weather", {})
    temp = round(fTocConversion(current.get("temperature")))
    wnd = round(wndSpeedtoMPH(current.get("windspeed")))
    windDir = wndDir(current.get("winddirection"))
    return temp,wnd,windDir

