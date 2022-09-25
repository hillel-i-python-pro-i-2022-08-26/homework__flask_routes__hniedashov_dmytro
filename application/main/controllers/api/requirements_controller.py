from application.constants import REQUIREMENTS_FILE_PATH
from application.main.decorators.app_route import AppRoute
from application.main.models.requirements import Requirements
from application.main.schemas.requirements import RequirementsSchema


@AppRoute.route("/")
def index():
    return RequirementsSchema().dump(Requirements(REQUIREMENTS_FILE_PATH)), 200
