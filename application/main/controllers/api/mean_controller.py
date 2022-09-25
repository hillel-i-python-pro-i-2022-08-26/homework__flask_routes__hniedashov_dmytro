from application.main.decorators.app_route import AppRoute
from application.main.factories.mean_factory import MeanFactory


@AppRoute.route("/")
def index():
    return MeanFactory().generate_with_data(data=("1", "2"))
