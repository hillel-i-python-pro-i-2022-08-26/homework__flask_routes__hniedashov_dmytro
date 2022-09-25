from flask import Blueprint

blueprint = Blueprint("space", __name__, url_prefix="/space")


@blueprint.route("/")
def index():
    return "SPACE"
