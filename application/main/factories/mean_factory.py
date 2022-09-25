from typing import Type
from application.main.factories.creator import Creator
from application.main.models.mean import Mean


class MeanFactory(Creator):
    def concrete(self) -> type[Mean]:
        return Mean

    def generate_with_data(self, data: tuple[float | int, float | int]):
        return (self.concrete())(*data)
