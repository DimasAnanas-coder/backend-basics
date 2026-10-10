from clients import rates, weather

from .preprocessing import get_preprocessed_rates, get_preprocessed_weather


def build_city_summary(city: str, currency: str = "USD") -> dict:
    row_weather = weather.get_weather(city)
    row_rate = rates.get_rate(currency)

    weather_data = get_preprocessed_weather(row_weather)
    rates_data = get_preprocessed_rates(row_rate, currency)

    return {
        "city": city,
        "weather": weather_data,
        "rates": rates_data,
    }
