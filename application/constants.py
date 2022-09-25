import pathlib
from typing import Final

APP_DIR_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parent
REQUIREMENTS_FILE_PATH: Final[pathlib.Path] = pathlib.Path(APP_DIR_PATH.parent, "requirements.txt")
CONTROLLERS_DIR_PATH: Final[pathlib.Path] = pathlib.Path(APP_DIR_PATH, "main", "controllers")
