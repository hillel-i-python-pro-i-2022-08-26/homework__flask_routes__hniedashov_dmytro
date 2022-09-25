import importlib.util
import pathlib
import types

from flask import Blueprint
from application.constants import CONTROLLERS_DIR_PATH


def load_controllers_as_child_blueprints(base: Blueprint) -> Blueprint:
    for controller in pathlib.Path(CONTROLLERS_DIR_PATH).glob("*.py"):

        if (module := load_module_with_blueprint(controller)) is not None:
            base.register_blueprint(module.blueprint)

    return base


def load_module_with_blueprint(controller: pathlib.Path) -> bool | types.ModuleType:
    spec = importlib.util.spec_from_file_location(controller.stem, controller.as_posix())

    if spec is None:
        return False

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module
