from faker import Faker
import time


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def login(self) -> str:
        return self.faker.user_name()
    
    def password(self) -> str:
        return f"{self.faker.password()}{time.time()}"
    
    def first_name(self) -> str:
        return self.faker.first_name()
    
fake = Fake(faker=Faker())
