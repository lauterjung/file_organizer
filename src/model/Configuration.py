import os
from exceptions.FileNotFound import FileNotFound


class Configuration:

    def __init__(self):
        file_path: str
        ORIGIN_ROOT_FOLDER: str
        DESTINATION_ROOT_FOLDER: str
        HAS_INTERMEDIATE_FOLDER: bool

    def file_exists(self, file_path) -> bool:
        if (os.path.isfile(file_path)):
            return True
        else:
            raise (FileNotFound)

    def set_from_json(self) -> None:
        return

    def read_json(self, filePath: str) -> str:
        return ""

    def validate_text_input(self) -> bool:
        return True