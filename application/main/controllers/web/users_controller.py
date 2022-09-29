from flask import render_template

from application.main.decorators.app_route import AppRoute
from application.main.services.users_service import UserService


@AppRoute.route("/generate")
@AppRoute.route("/generate/<int:quantity>")
def index(quantity: int = 100):
    return render_template("users.html", users=UserService.get_users(quantity=quantity), quantity=quantity)
