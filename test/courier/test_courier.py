from clients.courier.courier_schema import CreateCourierBadRequestSchema, CreateCourierRequestSchema, CreateCourierResponseSchema, CreateCourierConflictResponseSchema, CreateCourierrBadRequesResponseSchema, LoginCourierNotFoundResponseSchema, LoginCourierRequestSchema, LoginCourierResponseSchema
from fixtures.courier import CourierFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courier import assert_bad_request_create_courier_response, assert_conflict_create_courier_response, assert_create_courier_response, assert_login_courier_response, assert_not_found_create_courier_response
from tools.fakers import fake
from tools.assertions.schema import validate_json_schema
from clients.courier.courier_client import CourierClient

from http import HTTPStatus
import pytest

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

    @pytest.mark.parametrize(
            "login, password", 
                [
                ("", ""), 
                ("", fake.password()), 
                (fake.login(), None), 
                (fake.login(), ""), 
                (None, fake.password())
                ])
    def test_create_without_required_parametres(self, courier_client: CourierClient, login, password):
        request = CreateCourierBadRequestSchema(login=login, password=password)
        response = courier_client.create_courier_api(request=request)
        response_data = CreateCourierrBadRequesResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.BAD_REQUEST)
        validate_json_schema(response.json(), schema=response_data.model_json_schema())
        assert_bad_request_create_courier_response(response=response_data)

    def test_login_courier(self, function_courier: CourierFixture, courier_client: CourierClient):
        request = LoginCourierRequestSchema(login=function_courier.request.login, password=function_courier.request.password)
        response = courier_client.login_courier_api(request=request)
        response_data = LoginCourierResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_login_courier_response(response=response_data)

    def test_login_courier_with_incorrect_login(
                                                            self, 
                                                            function_courier: CourierFixture, 
                                                            courier_client: CourierClient
                                                            ):
        request = LoginCourierRequestSchema(login=fake.login(), password=function_courier.request.password)
        response = courier_client.login_courier_api(request=request)
        response_data = LoginCourierNotFoundResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.NOT_FOUND)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_not_found_create_courier_response(response=response_data)

    def test_login_courier_with_incorrect_password(
                                                            self, 
                                                            function_courier: CourierFixture, 
                                                            courier_client: CourierClient
                                                            ):
        request = LoginCourierRequestSchema(login=function_courier.request.login, password=fake.password())
        response = courier_client.login_courier_api(request=request)
        response_data = LoginCourierNotFoundResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.NOT_FOUND)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_not_found_create_courier_response(response=response_data)