from clients.orders.orders_client import OrdersClient
from clients.orders.orders_schema import GetOrdersResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code

from http import HTTPStatus
import allure


class TestGetOrders:
    @allure.title("Get orders list")
    def test_get_orders(self, orders_client: OrdersClient):
        response = orders_client.get_orders_api()
        response_data = GetOrdersResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())