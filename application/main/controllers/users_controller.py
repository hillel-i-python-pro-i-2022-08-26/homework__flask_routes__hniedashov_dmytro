from flask import Blueprint
from application.main.schemas.user import UserSchema
from application.main.services.users_service import UserService

blueprint = Blueprint("users", __name__, url_prefix="/users")


@blueprint.route("/generate")
@blueprint.route("/generate/<int:quantity>")
def generate(quantity: int = 100):
    return UserSchema(many=True).dump(UserService.get_users(quantity=quantity)), 200
