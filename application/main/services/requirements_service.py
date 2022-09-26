import itertools
from application.constants import REQUIREMENTS_FILE_PATH
from application.main.models.requirements import Requirements
from itertools import groupby


class RequirementsService:
    @staticmethod
    def get() -> Requirements:
        return Requirements(REQUIREMENTS_FILE_PATH)

    @staticmethod
    def get_parsed():
        requirements = RequirementsService.get()
        grouped = [list(group) for k, group in groupby(requirements.content, lambda x: "#" in x) if not k]
        packages = itertools.chain(*grouped)

        return [tuple(package.split("==")) for package in packages if package]
