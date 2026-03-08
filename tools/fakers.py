from faker import Faker


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def login(self) -> str:
        return self.faker.user_name()
    
    def password(self) -> str:
        return self.faker.password()
    
    def first_name(self) -> str:
        return self.faker.first_name()
    
fake = Fake(faker=Faker())