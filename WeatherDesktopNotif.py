import requests
from plyer import notification


def get_coordinates(city):
    """Fetch latitude and longitude for a given city."""
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    try:
        res = requests.get(
            geo_url, params={"name": city, "count": 1}, timeout=10)
        res.raise_for_status()
        data = res.json()
        if "results" in data and data["results"]:
            return data["results"][0]["latitude"], data["results"][0]["longitude"]
    except Exception as e:
        print(f"❌ Error fetching coordinates: {e}")
    return None, None


def get_weather(lat, lon):
    """Fetch current weather data from Open-Meteo API."""
    weather_url = "https://api.open-meteo.com/v1/forecast"
    try:
        res = requests.get(weather_url, params={
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }, timeout=10)
        res.raise_for_status()
        data = res.json()
        return data.get("current_weather")
    except Exception as e:
        print(f"❌ Error fetching weather: {e}")
    return None


def show_notification(city, temp, wind):
    """Show a desktop notification with weather info."""
    weather_info = f"{city}: {temp}°C, Wind {wind} km/h"
    print("🌦️ Weather:", weather_info)
    notification.notify(
        title="Weather Update",
        message=weather_info,
        timeout=5
    )


def main():
    city = input("Enter city name: ").strip() or "Delhi"
    lat, lon = get_coordinates(city)

    if lat is None or lon is None:
        print("⚠️ City not found.")
        return

    weather = get_weather(lat, lon)
    if weather:
        show_notification(city, weather["temperature"], weather["windspeed"])
    else:
        print("⚠️ Weather data not found.")


if __name__ == "__main__":
    main()
