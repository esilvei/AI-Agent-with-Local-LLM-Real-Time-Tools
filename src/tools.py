import requests
from langchain_core.tools import Tool
from src.config import api_key


def calculator_func(expression: str) -> str:
    """Calculates mathematical expressions securely."""
    try:
        safe_expr = "".join([c for c in expression if c in "0123456789+-*/()."])
        if not safe_expr:
            return "Error: Invalid input."
        result = str(eval(safe_expr))
        return result
    except Exception as e:
        return f"Calculation error: {e}"


def weather_tool(city: str) -> str:
    """Queries real-time weather via OpenWeatherMap API."""
    # 1. Input cleanup
    city_clean = city.replace("Action Input:", "").strip()
    if "None" in city_clean or len(city_clean) < 2:
        return "Error: Specify the city. Example: 'London'"

    # 2. Retrieve Key (Security)
    if not api_key:
        return "Configuration Error: OpenWeather API Key not found in .env."

    # 3. Real API Call
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_clean,
        "appid": api_key,
        "units": "metric",  # For Celsius
        "lang": "en",  # For English description
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"The current weather in {city_clean} is: {desc} with {temp}°C."
        else:
            return f"Weather API Error: {data.get('message', 'Unknown')}"

    except Exception as e:
        return f"Connection error: {e}"


def get_tools():
    return [
        Tool(
            name="Calculator",
            func=calculator_func,
            description="Useful for math. Input must be ONLY the mathematical expression.",
        ),
        Tool(
            name="Weather",
            func=weather_tool,
            description="Useful for weather. Input must be ONLY the city name.",
        ),
    ]
