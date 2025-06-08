from flask import Blueprint, render_template
import requests

weather_bp = Blueprint('weather_bp', __name__)

@weather_bp.route("/weather_current", methods=["GET", "POST"])
def weather_current():
    lat, lon = 36.87, -95.11  # Welch, OK
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    current = data.get("current_weather", {})
    temp = current.get("temperature")
    wnd = current.get("windspeed")
    wndDir = current.get("winddirection")
    c2fconvert = (temp * 1.8) + 32
    return render_template("weather-current.html", weather=c2fconvert, windSpeed=wnd, windDirection=wndDir)
