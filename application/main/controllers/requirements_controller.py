from flask import Blueprint
from application.constants import REQUIREMENTS_FILE_PATH
from application.main.models.requirements import Requirements
from application.main.schemas.requirements import RequirementsSchema

blueprint = Blueprint("requirements", __name__, url_prefix="/requirements")


@blueprint.route("/")
def index():
    return RequirementsSchema().dump(Requirements(REQUIREMENTS_FILE_PATH)), 200
