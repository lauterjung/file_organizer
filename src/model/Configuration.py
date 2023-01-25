import json
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
            raise FileNotFound

    def read_json(self, filePath: str) -> dict:
        data: dict  
        
        with open(filePath, 'r') as json_file:
            data = json.load(json_file)
        
        return data

    def validate_json_keys(self, json_data: dict) -> bool:
        return True
    
    def validate_text_input(self, json_data: dict) -> bool:
        return True
    
    def set_from_json(self) -> None:
        return