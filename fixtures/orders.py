import pytest

from clients.orders.orders_client import OrdersClient, get_order_client


@pytest.fixture
def orders_client() -> OrdersClient:
    return get_order_client()