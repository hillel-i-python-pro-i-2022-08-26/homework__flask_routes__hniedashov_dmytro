from application.main.decorators.app_route import AppRoute
from application.main.schemas.requirements import RequirementsSchema
from application.main.services.requirements_service import RequirementsService


@AppRoute.route("/")
def index():
    return RequirementsSchema().dump(RequirementsService.get()), 200
