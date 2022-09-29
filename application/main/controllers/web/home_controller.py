from flask import render_template
from application.main.decorators.app_route import AppRoute


@AppRoute.route("/", use_prefix=False)
def index():
    return render_template("index.html")
