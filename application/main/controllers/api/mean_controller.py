from application.main.decorators.app_route import AppRoute
from application.main.services.mean_service import MeanService


@AppRoute.route("/")
def index():
    return MeanService().get_mean_pretty()
