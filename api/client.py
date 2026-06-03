import requests


class ApiClient:
    def __init__(self, base_url):
        self._base_url = base_url
        self._session = requests.Session()
        self._session.headers.update({"Content-Type": "application/x-www-form-urlencoded"})

    def get(self, endpoint, **kwargs):
        return self._session.get(f"{self._base_url}{endpoint}", **kwargs)

    def post(self, endpoint, **kwargs):
        return self._session.post(f"{self._base_url}{endpoint}", **kwargs)

    def put(self, endpoint, **kwargs):
        return self._session.put(f"{self._base_url}{endpoint}", **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._session.delete(f"{self._base_url}{endpoint}", **kwargs)

    def close(self):
        self._session.close()
