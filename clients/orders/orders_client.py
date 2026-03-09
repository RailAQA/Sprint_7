from clients.public_http_builder import get_public_http_client
from clients.api_client import ApiClient
from clients.orders.orders_schema import CreateOrderRequestSchema

from requests import Response


class OrdersClient(ApiClient):
    def create_order_api(self, request: CreateOrderRequestSchema) -> Response:
        request_data = request.model_dump(by_alias=True)
        return self.post(url="/api/v1/orders", json=request_data)
    
    def get_orders_api(self) -> Response:
        return self.get("/api/v1/orders")
    
def get_order_client() -> OrdersClient:
    return OrdersClient(client=get_public_http_client())