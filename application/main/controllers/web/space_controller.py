from flask import render_template

from application.main.decorators.app_route import AppRoute
from application.main.services.space_service import SpaceService

space_service = SpaceService()


@AppRoute.route("/")
def astros():
    astros_info = space_service.get_astros_full_info()
    return render_template("space_astros.html", people=astros_info.get("people"), count=astros_info.get("number"))


@AppRoute.route("/location")
def location():
    return render_template("space_location.html", position=space_service.get_current_location())
