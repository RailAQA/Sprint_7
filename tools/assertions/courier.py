from tools.assertions.base import assert_equal
from clients.courier.courier_schema import CreateCourierResponseSchema, CreateCourierConflictResponseSchema


def assert_create_courier_response(response: CreateCourierResponseSchema):
    assert_equal(actual=response.ok, expected=True, name="ok")

def assert_conflict_create_courier_response(response: CreateCourierConflictResponseSchema):
    assert_equal(actual=response.code, expected=409, name="code")
    assert_equal(actual=response.message, expected="Этот логин уже используется. Попробуйте другой.", name="message")