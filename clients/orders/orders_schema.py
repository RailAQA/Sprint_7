from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake


class CreateOrderRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    address: str = Field(default_factory=fake.address)
    metro_station: int = Field(alias="metroStation", default_factory=fake.stations)
    phone: str = Field(default_factory=fake.phone)
    rent_time: int = Field(alias="rentTime", default_factory=fake.rent_time)
    delivery_date: str = Field(alias="deliveryDate", default_factory=fake.delivery_date)
    comment: str = Field(default_factory=fake.comment)
    color: list[str] | None = Field(default_factory=fake.color)

class CreateOrderResponseSchema(BaseModel):
    track: int

class Orders(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    courier_id: int | None = Field(alias="courierId")
    first_name: str | None = Field(alias="firstName")
    last_name: str | None = Field(alias="lastName")
    address: str | None
    metro_station: str | None = Field(alias="metroStation")
    phone: str | None
    rent_time: int | None = Field(alias="rentTime")
    delivery_date: str | None = Field(alias="deliveryDate")
    track: int
    color: list[str] | None
    comment: str | None
    created_at: str = Field(alias="createdAt")
    updated_at: str = Field(alias="updatedAt")
    status: int

class PageInfo(BaseModel):
    page: int
    total: int
    limit: int

class Stations(BaseModel):
    name: str
    number: str
    color: str

class GetOrdersResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    orders: list[Orders]
    page_info: PageInfo = Field(alias="pageInfo")
    available_stations: list[Stations] = Field(alias="availableStations")