from clients.api_client import ApiClient
from clients.courier.courier_schema import CreateCourierRequestSchema
from requests import Response


class CourierClient(ApiClient):
    def create_courier_api(self, request: CreateCourierRequestSchema) -> Response:
        return self.post(url="/api/v1/courier", json=request)