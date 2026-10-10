from .http import HttpClient

CITY_COORDINATES = {
    "Moscow": (55.7558, 37.6173),
    "Saratov": (51.5333, 46.0333),
}


class WeatherClient(HttpClient):
    base_url = "https://api.open-meteo.com/v1/forecast"

    def __init__(self, city: str) -> None:
        url = self.build_url(city)
        super().__init__(url)

    def build_url(self, city: str) -> str:
        try:
            latitude, longitude = CITY_COORDINATES[city]
        except KeyError:
            raise ValueError(f"City '{city}' is not supported.")
        
        return f"{self.base_url}?latitude={latitude}&longitude={longitude}&current_weather=true"

    def get(self) -> dict:
        json_response = self.get_response()
        #print(json_response)
        current_weather = json_response.get("current_weather", {})
        return {
            "temperature": current_weather.get("temperature"),
        }

def get_weather(city: str) -> dict:
    weather_client = WeatherClient(city)
    return weather_client.get()
