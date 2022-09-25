from application.main.factories.user_factory import UserFactory
from application.main.models.user import User


class UserService:
    @staticmethod
    def get_user() -> User:
        return UserFactory().concrete()

    @staticmethod
    def get_users(quantity: int = 100) -> list[User]:
        return [UserService.get_user() for _ in range(quantity)]
