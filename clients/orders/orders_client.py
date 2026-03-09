from clients.public_http_builder import get_public_http_client
from tools.routes import AppRoute
from clients.api_client import ApiClient
from clients.orders.orders_schema import CreateOrderRequestSchema

from requests import Response
import allure


class OrdersClient(ApiClient):
    @allure.step("Login order")
    def create_order_api(self, request: CreateOrderRequestSchema) -> Response:
        request_data = request.model_dump(by_alias=True)
        return self.post(url=AppRoute.CREATE_ORDER, json=request_data)
    
    @allure.step("Get orders list")
    def get_orders_api(self) -> Response:
        return self.get(AppRoute.GET_ORDER)
        
def get_order_client() -> OrdersClient:
    return OrdersClient(client=get_public_http_client())