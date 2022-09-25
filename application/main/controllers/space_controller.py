from flask import Blueprint
from application.main.services.space_service import SpaceService

blueprint = Blueprint("space", __name__, url_prefix="/space")
space_service = SpaceService()


@blueprint.route("/")
def astros():
    return space_service.get_astros()


@blueprint.route("/location")
def location():
    return space_service.get_current_location()
