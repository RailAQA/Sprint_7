from clients.courier.courier_client import CourierClient
from clients.courier.courier_client import get_courier_client

import pytest

@pytest.fixture
def courier_client() -> CourierClient:
    return get_courier_client()