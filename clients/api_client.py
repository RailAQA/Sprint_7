from requests import Session, Response


class ApiClient:
    def __init__(self, client: Session):
        self.client = client

    def get(self, url: str, params = None) -> Response:
        return self.client.get(url=url, params=params)

    def post(self, url: str, data = None, json = None) -> Response:
        return self.client.post(url=url, data=data, json=json)