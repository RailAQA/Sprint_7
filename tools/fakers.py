from faker import Faker
from tools.data.get_stations import get_stations

import time


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def login(self) -> str:
        return f"test_{self.faker.user_name()}{time.time()}"
    
    def password(self) -> str:
        return self.faker.password()
    
    def first_name(self) -> str:
        return self.faker.first_name()
    
    def last_name(self) -> str:
        return self.faker.last_name()
    
    def address(self) -> str:
        return self.faker.address()
    
    def stations(self) -> int:
        stations_data = get_stations()
        return int(self.faker.random_choices(stations_data, length=1)[0])
    
    def phone(self) -> str:
        return self.faker.basic_phone_number()
    
    def rent_time(self) -> int:
        return self.faker.random_int(min=1, max=30)
    
    def delivery_date(self) -> str:
        return str(self.faker.date_this_month(before_today=False, after_today=True))
    
    def comment(self) -> str:
        return self.faker.sentence()
    
    def color(self) -> list[str]:
        data = []
        data.append(self.faker.color_name())
        return data
    
fake = Fake(faker=Faker())
