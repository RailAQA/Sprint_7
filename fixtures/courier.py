from clients.courier.courier_client import CourierClient
from clients.courier.courier_client import get_courier_client
from clients.courier.courier_schema import CreateCourierRequestSchema, CreateCourierConflictResponseSchema

import pytest
from pydantic import BaseModel


class CourierFixture(BaseModel):
    request: CreateCourierRequestSchema

@pytest.fixture(scope="module")
def courier_client() -> CourierClient:
    return get_courier_client()

@pytest.fixture
def function_courier(courier_client: CourierClient) -> CourierFixture:
    request = CreateCourierRequestSchema()
    response = courier_client.create_courier_api(request=request)
    return CourierFixture(request=request)

@pytest.fixture(scope="class")
def class_courier(courier_client: CourierClient) -> CourierFixture:
    request = CreateCourierRequestSchema(login="test2836", password="12345")
    response = courier_client.create_courier_api(request=request)
    return CourierFixture(request=request)