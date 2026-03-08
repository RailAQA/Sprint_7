from requests_toolbelt import sessions
from requests import Session


def get_public_http_client() -> Session:
    return sessions.BaseUrlSession(base_url="https://qa-scooter.praktikum-services.ru")