import requests
from langchain.tools import tool

@tool
def get_weather(city: str) -> dict:
    """
    Get current weather information for a city using OpenWeatherMap API.

    Args:
        city (str): The name of the city (e.g., "Lahore", "New York")

    Returns:
        dict: Weather data or an error message.
    """
    try:
        my_weather_api_key = "175f6983268832530710935a33d3240b"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_weather_api_key}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            description = data["weather"][0]["description"].capitalize() 
            temperature = data["main"]["temp"]                             
            feels_like = data["main"]["feels_like"]

            return {
                "tool": "weather",
                "city": city.title(),
                "description": description,
                "temperature": f"{temperature}°C",                       
                "feels_like": f"{feels_like}°C"
            }

        else:
            return {
                "error": f"🌧️ Could not find weather for '{city}'.",
                "status_code": response.status_code
            }

    except Exception as e:
        return {
            "error": f"🌩️ Oops! Something went wrong: {str(e)}",
            "city": city
        }
