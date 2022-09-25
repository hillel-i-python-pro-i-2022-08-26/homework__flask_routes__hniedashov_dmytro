from flask import Blueprint
from application.main.controllers_loader import load_controllers_as_child_blueprints

api_blueprint = load_controllers_as_child_blueprints(Blueprint("api", "api", url_prefix="/api"))
