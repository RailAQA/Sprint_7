from clients.api_client import ApiClient
import allure
from requests import Response

from clients.courier.courier_schema import CreateCourierRequestSchema, LoginCourierRequestSchema
from tools.routes import AppRoute
from clients.public_http_builder import get_public_http_client


class CourierClient(ApiClient):
    @allure.step("Create courier")
    def create_courier_api(self, request: CreateCourierRequestSchema) -> Response:
        request_data = request.model_dump(by_alias=True)
        return self.post(url=AppRoute.CREATE_COURIER, json=request_data)
    
    @allure.step("Login courier")
    def login_courier_api(self, request: LoginCourierRequestSchema) -> Response:
        request_data = request.model_dump(by_alias=True)
        return self.post(url=AppRoute.LOGIN_COURIER, json=request_data)
    
    @allure.step("Delete courier")
    def delete_courier(self, id: str) -> Response:
        return self.delete(url=f"{AppRoute.DELETE_COURIER}{id}")
    
def get_courier_client() -> CourierClient:
    return CourierClient(client=get_public_http_client())
