from application.main import faker
from dataclasses import dataclass


@dataclass
class User:
    name: str = ""

    @property
    def last_name(self) -> str:
        return faker.last_name()

    @property
    def email(self) -> str:
        return f"{self.name.lower()}@{faker.domain_name()}"

    def __post_init__(self):
        self.name = faker.first_name()
