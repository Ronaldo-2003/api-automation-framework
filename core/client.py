import requests
from core.config import BASE_URL, TIMEOUT


class APIClient:
    def __init__(self):
        self.session = requests.Session()

    def get(self, endpoint):
        return self.session.get(
            f"{BASE_URL}{endpoint}",
            timeout=TIMEOUT
        )

    def post(self, endpoint, payload):
        return self.session.post(
            f"{BASE_URL}{endpoint}",
            json=payload,
            timeout=TIMEOUT
        )

    def put(self, endpoint, payload):
        return self.session.put(
            f"{BASE_URL}{endpoint}",
            json=payload,
            timeout=TIMEOUT
        )

    def delete(self, endpoint):
        return self.session.delete(
            f"{BASE_URL}{endpoint}",
            timeout=TIMEOUT
        )
