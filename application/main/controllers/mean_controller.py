from flask import Blueprint

blueprint = Blueprint("mean", __name__, url_prefix="/mean")


@blueprint.route("/")
def index():
    return "MEAN"
