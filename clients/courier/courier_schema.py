from pydantic import BaseModel, Field, ConfigDict


class CreateCourierRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    login: str
    password: str
    first_name: str = Field(alias="firstName")