def get_weather(city: str) -> dict:
    weather_data = {
        "Moscow": {"temperature": 5.0, "description": "Rainy"},
        "Saratov": {"temperature": 10.0, "description": "Sunny"},
    }
    return weather_data.get(city, {"temperature": 0.0, "description": "Unknown"})