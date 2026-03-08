from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake


class CreateCourierRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    login: str = Field(default_factory=fake.login)
    password: str = Field(default_factory=fake.password)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)

class CreateCourierResponseSchema(BaseModel):
    ok: bool = True
