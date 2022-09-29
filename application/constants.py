import pathlib
from typing import Final

"""
Bunch of useful paths inside the application
"""
APP_DIR_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parent
MAIN_DIR_PATH: Final[pathlib.Path] = APP_DIR_PATH.parent
TEMPLATES_FOLDER_PATH: Final[pathlib.Path] = pathlib.Path(MAIN_DIR_PATH, "templates")
MEAN_FILE_PATH: Final[pathlib.Path] = pathlib.Path(APP_DIR_PATH.parent, "public", "mean.csv")
REQUIREMENTS_FILE_PATH: Final[pathlib.Path] = pathlib.Path(APP_DIR_PATH.parent, "requirements.txt")
CONTROLLERS_DIR_PATH: Final[pathlib.Path] = pathlib.Path(APP_DIR_PATH, "main", "controllers")

"""
Other useful constants
"""
MEAN_FILE_LINK: str = "https://drive.google.com/uc?export=download&format=csv&id=1yM0a4CSf0iuAGOGEljdb7qcWyz82RBxl"
INCHES_TO_CM_INDEX: float = 2.54
POUNDS_TO_KG_INDEX: float = 0.453592
