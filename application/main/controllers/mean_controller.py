from flask import Blueprint
from application.main.factories.mean_factory import MeanFactory

blueprint = Blueprint("mean", __name__, url_prefix="/mean")


@blueprint.route("/")
def index():
    return MeanFactory().generate_with_data(data=("1", "2"))
