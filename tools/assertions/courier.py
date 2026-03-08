from tools.assertions.base import assert_equal
from clients.courier.courier_schema import CreateCourierResponseSchema, CreateCourierConflictResponseSchema, CreateCourierrBadRequesResponseSchema

from http import HTTPStatus


def assert_create_courier_response(response: CreateCourierResponseSchema):
    assert_equal(actual=response.ok, expected=True, name="ok")

def assert_conflict_create_courier_response(response: CreateCourierConflictResponseSchema):
    assert_equal(actual=response.code, expected=HTTPStatus.CONFLICT, name="code")
    assert_equal(actual=response.message, expected="Этот логин уже используется. Попробуйте другой.", name="message")

def assert_bad_request_create_courier_response(response: CreateCourierrBadRequesResponseSchema):
    assert_equal(actual=response.code, expected=HTTPStatus.BAD_REQUEST, name="code")
    assert_equal(actual=response.message, expected="Недостаточно данных для создания учетной записи", name="message")