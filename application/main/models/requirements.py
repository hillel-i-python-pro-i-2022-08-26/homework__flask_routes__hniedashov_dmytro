import pathlib
from dataclasses import dataclass


@dataclass
class Requirements:
    file_path: pathlib.Path

    @property
    def content(self) -> list[str]:
        return self.file_path.read_text().splitlines()
