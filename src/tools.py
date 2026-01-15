import requests
from langchain_core.tools import Tool
from src.config import api_key


def calculator_func(expression: str) -> str:
    """Calculates mathematical expressions securely."""
    try:
        # Sanitization: keep only numbers and basic operators
        safe_expr = "".join([c for c in expression if c in "0123456789+-*/(). "])
        if not safe_expr.strip():
            return "\nResult: Error - Invalid input.\n"

        result = str(eval(safe_expr))
        # Adding newlines ensures the Agent sees this as a clean observation block
        return f"\nCalculation Result: {result}\n"
    except Exception as e:
        return f"\nCalculation error: {e}\n"


def weather_tool(city: str) -> str:
    """Queries real-time weather via OpenWeatherMap API."""
    # 1. Input cleanup
    city_clean = city.replace("Action Input:", "").strip()
    if "None" in city_clean or len(city_clean) < 2:
        return "\nError: Specify a valid city name.\n"

    # 2. Retrieve Key (Security check)
    if not api_key:
        return "\nConfiguration Error: OpenWeather API Key not found.\n"

    # 3. API Call
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_clean,
        "appid": api_key,
        "units": "metric",
        "lang": "en",
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            # Clean formatting for the agent to parse easily
            return f"\nWeather Data: The current weather in {city_clean} is {desc} with {temp}°C.\n"
        else:
            return f"\nWeather API Error: {data.get('message', 'Unknown city')}\n"

    except Exception as e:
        return f"\nConnection error: Could not reach weather service. {e}\n"


def get_tools():
    return [
        Tool(
            name="Calculator",
            func=calculator_func,
            description="Useful for math. Input must be ONLY the mathematical expression (e.g., '128*46').",
        ),
        Tool(
            name="Weather",
            func=weather_tool,
            description="Useful for weather updates. Input must be ONLY the city name.",
        ),
    ]
