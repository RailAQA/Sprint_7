from clients.courier.courier_schema import CreateCourierRequestSchema, CreateCourierResponseSchema, CreateCourierConflictResponseSchema
from fixtures.courier import CourierFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courier import assert_conflict_create_courier_response, assert_create_courier_response
from tools.assertions.schema import validate_json_schema
from clients.courier.courier_client import CourierClient

from http import HTTPStatus

class TestCourier:
    def test_create_courier(self, courier_client: CourierClient):
        request = CreateCourierRequestSchema()
        response = courier_client.create_courier_api(request=request)
        response_data = CreateCourierResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_create_courier_response(response=response_data)

    def test_create_duplicate_courier(self, function_courier: CourierFixture, courier_client: CourierClient):
        request = function_courier.request
        response = courier_client.create_courier_api(request=request)
        response_data = CreateCourierConflictResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.CONFLICT)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_conflict_create_courier_response(response=response_data)