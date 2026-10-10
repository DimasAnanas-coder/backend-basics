def get_rate(currency: str) -> float:
    rates = {
        "USD": 80.0,
        "EUR": 90.0,
        "GBP": 95.0,
        "JPY": 101.0,
    }
    return rates.get(currency, 0.0)