from flask import Flask
from faker import Faker
from .config import configurations

faker = Faker()


def create_app(app_config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(configurations[app_config])

    return app
