from clients.courier.courier_client import CourierClient
from clients.courier.courier_client import get_courier_client
from clients.courier.courier_schema import CreateCourierRequestSchema, CreateCourierConflictResponseSchema, LoginCourierRequestSchema

import pytest
from pydantic import BaseModel
from _pytest.fixtures import SubRequest
from typing import Generator


class CourierFixture(BaseModel):
    request: CreateCourierRequestSchema

@pytest.fixture(scope="module")
def courier_client() -> CourierClient:
    return get_courier_client()

@pytest.fixture
def function_courier(courier_client: CourierClient) -> Generator[CourierFixture, None, None]:
    request = CreateCourierRequestSchema()
    courier_client.create_courier_api(request=request)
    yield CourierFixture(request=request)

    login_request = LoginCourierRequestSchema(login=request.login, password=request.password)
    courier_id = courier_client.login_courier_api(request=login_request).json().get("id")
    courier_client.delete_courier(id=courier_id)
    
@pytest.fixture
def function_bad_request_courier(request: SubRequest, function_courier: CourierFixture):
    case_type = request.param
    cases = {
        "empty_login": {"login": "", "password": function_courier.request.password},
        "null_login": {"login": None, "password": function_courier.request.password},
        "empty_password": {"login": function_courier.request.login, "password": ""},
        "null_password": {"login": function_courier.request.login, "password": None},
        "empty_login_and_password": {"login": "", "password": ""},
        "null_login_and_password": {"login": None, "password": None},
    }
    
    return cases[case_type]