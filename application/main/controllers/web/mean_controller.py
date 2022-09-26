from flask import render_template
from application.main.decorators.app_route import AppRoute
from application.main.services.mean_service import MeanService


@AppRoute.route("/")
def index():
    return render_template("mean.html", mean=MeanService().get_mean_metric_rounded())
