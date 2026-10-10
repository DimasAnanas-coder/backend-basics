from .http import HttpClient


class RatesClient(HttpClient):
    base_url = " https://api.frankfurter.dev/v2/rate"

    def __init__(self, currency: str) -> None:
        url = self.build_url(currency)
        super().__init__(url)

    def build_url(self, currency: str) -> str:
        return f"{self.base_url}/{currency}/RUB"

    def get(self) -> dict:
        return self.get_response()


def get_rate(currency: str) -> float:
    rates_client = RatesClient(currency)
    return rates_client.get().get("rate")
