from application.main.decorators.app_route import AppRoute
from application.main.services.space_service import SpaceService

space_service = SpaceService()


@AppRoute.route("/")
def astros():
    return space_service.get_astros()


@AppRoute.route("/location")
def location():
    return space_service.get_current_location()
