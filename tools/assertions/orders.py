from tools.assertions.base import assert_is_true
from clients.orders.orders_schema import CreateOrderResponseSchema

def assert_create_order_response(response: CreateOrderResponseSchema):
    assert_is_true(actual=response.track, name="track")