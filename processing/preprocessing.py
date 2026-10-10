def get_preprocessed_weather(row_weather: dict) -> dict:
    temp_c = row_weather.get("temperature")
    is_need_warm_clothes = temp_c < 10.0

    return {"temp_c": temp_c, "warm_clothes": is_need_warm_clothes}


def get_preprocessed_rates(row_rate: float, currency: str) -> dict:
    is_expensive = row_rate > 100

    return {
        "currency": currency,
        "rate_to_rub": row_rate,
        "expensive": is_expensive,
    }
