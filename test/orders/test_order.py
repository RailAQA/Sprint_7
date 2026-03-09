from clients.orders.orders_client import OrdersClient
from clients.orders.orders_schema import CreateOrderRequestSchema, CreateOrderResponseSchema, GetOrdersResponseSchema
from tools.assertions.orders import assert_create_order_response
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code

from http import HTTPStatus
import pytest


class TestOrders:
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], [], None])
    def test_create_order(self, orders_client: OrdersClient, color):
        request = CreateOrderRequestSchema(color=color)
        response = orders_client.create_order_api(request=request)
        response_data = CreateOrderResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_create_order_response(response=response_data)

    def test_get_orders(self, orders_client: OrdersClient):
        response = orders_client.get_orders_api()
        response_data = GetOrdersResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())