import pathlib
from typing import Final

"""
Bunch of useful paths inside the application
"""
APP_DIR_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parent
REQUIREMENTS_FILE_PATH: Final[pathlib.Path] = pathlib.Path(APP_DIR_PATH.parent, "requirements.txt")
CONTROLLERS_DIR_PATH: Final[pathlib.Path] = pathlib.Path(APP_DIR_PATH, "main", "controllers")

"""
Other useful constants
"""
INCHES_TO_CM_INDEX: float = 2.54
POUNDS_TO_KG_INDEX: float = 0.453592
