import importlib.util
import pathlib
import sys
import types

from flask import Blueprint, Flask
from application.constants import CONTROLLERS_DIR_PATH, TEMPLATES_FOLDER_PATH
from application.main.decorators.app_route import AppRoute


def load_controllers(app: Flask) -> None:
    namespaces = [namespace for namespace in pathlib.Path(CONTROLLERS_DIR_PATH).rglob("*") if namespace.is_dir()]

    for i, controller_namespace_path in enumerate(namespaces):
        name = controller_namespace_path.stem

        if name == "__pycache__":
            continue

        prefix = name if name != "web" else ""

        namespaced_blueprint = Blueprint(
            name, name, url_prefix=f"/{prefix}", template_folder=str(TEMPLATES_FOLDER_PATH)
        )

        for controller in controller_namespace_path.glob("*.py"):
            load_module_with_routes(controller)

        for blueprint in AppRoute.blueprints.values():
            namespaced_blueprint.register_blueprint(blueprint)

        AppRoute.clear_blueprints()
        app.register_blueprint(namespaced_blueprint)


def load_module_with_routes(controller: pathlib.Path) -> bool | types.ModuleType:
    spec = importlib.util.spec_from_file_location(controller.stem, controller.as_posix())

    if spec is None:
        return False

    module = importlib.util.module_from_spec(spec)
    sys.modules[module.__name__] = module
    spec.loader.exec_module(module)
