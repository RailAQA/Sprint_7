from clients.api_client import ApiClient
from requests import Response

from clients.courier.courier_schema import CreateCourierRequestSchema
from clients.public_http_builder import get_public_http_client


class CourierClient(ApiClient):
    def create_courier_api(self, request: CreateCourierRequestSchema) -> Response:
        return self.post(url="/api/v1/courier", json=request)
    
def get_courier_client() -> CourierClient:
    return CourierClient(client=get_public_http_client)
