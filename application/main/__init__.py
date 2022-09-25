from flask import Flask
from faker import Faker
from .config import configurations
from .controllers_loader import load_controllers

faker = Faker()


def create_app(app_config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(configurations[app_config])
    load_controllers(app)

    return app
