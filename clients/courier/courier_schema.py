from pydantic import BaseModel, Field, ConfigDict
from http import HTTPStatus

from tools.fakers import fake


class CreateCourierRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    login: str = Field(default_factory=fake.login)
    password: str = Field(default_factory=fake.password)
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)

class CreateCourierResponseSchema(BaseModel):
    ok: bool = True

class CreateCourierConflictResponseSchema(BaseModel):
    code: HTTPStatus = Field(default=HTTPStatus.CONFLICT)
    message: str = "Этот логин уже используется"

class CreateCourierBadRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    login: str | None = Field(default_factory=fake.login)
    password: str | None = Field(default_factory=fake.password)
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)

class CreateCourierrBadRequesResponseSchema(BaseModel):
    code: HTTPStatus = Field(default=HTTPStatus.BAD_REQUEST)
    message: str = "Недостаточно данных для создания учетной записи"

class LoginCourierRequestSchema(BaseModel):
    login: str
    password: str

class LoginCourierResponseSchema(BaseModel):
    id: int