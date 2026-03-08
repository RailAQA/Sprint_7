from tools.assertions.base import assert_equal
from clients.courier.courier_schema import CreateCourierResponseSchema


def assert_create_user_response(response: CreateCourierResponseSchema):
    assert response.ok == True
