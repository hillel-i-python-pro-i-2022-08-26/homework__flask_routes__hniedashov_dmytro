from application.main.decorators.app_route import AppRoute
from application.main.schemas.user import UserSchema
from application.main.services.users_service import UserService


@AppRoute.route("/generate")
@AppRoute.route("/generate/<int:quantity>")
def generate(quantity: int = 100):
    return UserSchema(many=True).dump(UserService.get_users(quantity=quantity)), 200
