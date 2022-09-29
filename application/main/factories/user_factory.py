from application.main.factories.creator import Creator
from application.main.models.user import User


class UserFactory(Creator):
    def concrete(self) -> type[User]:
        return User
