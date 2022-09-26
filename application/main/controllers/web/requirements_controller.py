from flask import render_template
from application.main.decorators.app_route import AppRoute
from application.main.services.requirements_service import RequirementsService


@AppRoute.route("/")
def index():
    return render_template("requirements.html", requirements=RequirementsService.get_parsed())
