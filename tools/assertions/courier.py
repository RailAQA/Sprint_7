from tools.assertions.base import assert_equal, assert_is_true
from clients.courier.courier_schema import CreateCourierResponseSchema, CreateCourierConflictResponseSchema, CreateCourierrBadRequesResponseSchema, LoginCourierResponseSchema, LoginCourierNotFoundResponseSchema, LoginCourierBadRequestResponseSchema

from http import HTTPStatus


def assert_create_courier_response(response: CreateCourierResponseSchema):
    assert_equal(actual=response.ok, expected=True, name="ok")

def assert_conflict_create_courier_response(response: CreateCourierConflictResponseSchema):
    assert_equal(actual=response.message, expected="Этот логин уже используется. Попробуйте другой.", name="message")

def assert_bad_request_create_courier_response(response: CreateCourierrBadRequesResponseSchema):
    assert_equal(actual=response.message, expected="Недостаточно данных для создания учетной записи", name="message")

def assert_login_courier_response(response: LoginCourierResponseSchema):
    assert_is_true(actual=response.id, name="id")

def assert_not_found_create_courier_response(response: LoginCourierNotFoundResponseSchema):
    assert_equal(actual=response.message, expected="Учетная запись не найдена", name="message")

def assert_bad_request_login_courier_response(response: LoginCourierBadRequestResponseSchema):
    assert_equal(actual=response.message, expected="Недостаточно данных для входа", name="message")