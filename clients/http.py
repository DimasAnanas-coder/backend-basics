import requests
import time

from abc import ABC, abstractmethod

REQUEST_TIMEOUT_S = 5
REQUEST_CONNECTION_TIMEOUT_S = 2
RETRIES_DELAY_S = 1
RETRIES_COUNT = 3

RETRIES_STATUS_CODES = {500, 502, 503, 504, 429}

class HttpClient(ABC):
    def __init__(self, url: str) -> None:
        self.url = url

    def get_response(self) -> dict:
        for attempt in range(RETRIES_COUNT):
            try:
                response = requests.get(
                    self.url,
                    timeout=(REQUEST_CONNECTION_TIMEOUT_S, REQUEST_TIMEOUT_S),
                )
                if response.status_code in RETRIES_STATUS_CODES:
                    time.sleep(RETRIES_DELAY_S)
                    continue
                response.raise_for_status()
                return response.json()
            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
                if attempt < RETRIES_COUNT - 1:
                    time.sleep(RETRIES_DELAY_S)
                else:
                    raise e

    @abstractmethod
    def get(self) -> dict:
        pass
