from clients.courier.courier_schema import LoginCourierBadRequestResponseSchema, LoginCourierBadRequestSchema, LoginCourierNotFoundResponseSchema, LoginCourierRequestSchema, LoginCourierResponseSchema
from fixtures.courier import CourierFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courier import assert_bad_request_login_courier_response, assert_login_courier_response, assert_not_found_create_courier_response
from tools.fakers import fake
from tools.assertions.schema import validate_json_schema
from clients.courier.courier_client import CourierClient

from http import HTTPStatus
import allure
import pytest


class TestLoginCourier:
    @allure.title("Login courier")
    def test_login_courier(self, function_courier: CourierFixture, courier_client: CourierClient):
        request = LoginCourierRequestSchema(login=function_courier.request.login, password=function_courier.request.password)
        response = courier_client.login_courier_api(request=request)
        response_data = LoginCourierResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_login_courier_response(response=response_data)

    class TestLoginCourierNegative:
        @allure.title("Login courier with incorrect login")
        def test_login_courier_with_incorrect_login(
                                                                self, 
                                                                courier_client: CourierClient,
                                                                function_courier: CourierFixture
                                                                ):
            request = LoginCourierRequestSchema(login=fake.login(), password=function_courier.request.password)
            response = courier_client.login_courier_api(request=request)
            response_data = LoginCourierNotFoundResponseSchema.model_validate_json(response.text)

            assert_status_code(actual=response.status_code, expected=HTTPStatus.NOT_FOUND)
            validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
            assert_not_found_create_courier_response(response=response_data)

        @allure.title("Login courier with incorrect password")
        def test_login_courier_with_incorrect_password(
                self, 
                courier_client: CourierClient,
                function_courier: CourierFixture
                ):
            request = LoginCourierRequestSchema(login=function_courier.request.login, password=fake.password())
            response = courier_client.login_courier_api(request=request)
            response_data = LoginCourierNotFoundResponseSchema.model_validate_json(response.text)

            assert_status_code(actual=response.status_code, expected=HTTPStatus.NOT_FOUND)
            validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
            assert_not_found_create_courier_response(response=response_data)

        @allure.title("Login courier without required paramtres")
        @pytest.mark.parametrize("function_bad_request_courier", 
                                [
                                    "empty_login",
                                    "null_login",
                                    "empty_password",
                                    "null_password",
                                    "empty_login_and_password",
                                    "null_login_and_password"
                                    ], indirect=True)
        def test_login_courier_without_required_parametres(self, courier_client: CourierClient, function_bad_request_courier):
            request = LoginCourierBadRequestSchema(login=function_bad_request_courier["login"], password=function_bad_request_courier["password"])
            response = courier_client.login_courier_api(request=request)
            response_data = LoginCourierBadRequestResponseSchema.model_validate_json(response.text)

            assert_status_code(actual=response.status_code, expected=HTTPStatus.BAD_REQUEST)
            validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
            assert_bad_request_login_courier_response(response=response_data)