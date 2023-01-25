import os
import shutil
import unittest
import sys
import json

from pathlib import Path
sys.path.insert(0, str(Path('src/').resolve()))
from src.exceptions.FileNotFound import FileNotFound
from src.model.Configuration import Configuration

class ConfigurationTests(unittest.TestCase):
    # move to setup?
    TEST_FOLDER_PATH: str = "tests/test_folder"
    FILE_NAME: str = "app_config.json"
    FILE_PATH: str = TEST_FOLDER_PATH + "/" + FILE_NAME
    VALID_JSON: dict = {
        "origin_root_folder": "a",
        "destination_root_folder": "a",
        "has_intermediate_folder": True,
        "file_types": [".a", ".b"],
        "patterns_to_match": ["*"]
        }
    VALID_JSON_STRING: str = json.dumps(VALID_JSON)
    INVALID_JSON_STRING: str = '{"A" "B"}'
    configuration: Configuration

    def setUp(self) -> None:
        if not os.path.exists(self.TEST_FOLDER_PATH):
            os.mkdir(self.TEST_FOLDER_PATH, mode=2)

        self.configuration = Configuration()

    def tearDown(self) -> None:
        if os.path.exists(self.TEST_FOLDER_PATH):
            shutil.rmtree(self.TEST_FOLDER_PATH, ignore_errors=True)

    def test_fileExists_FileNotFound_RaisesException(self):
        with self.assertRaises(Exception) as context:
            self.configuration.file_exists(self.FILE_PATH)

        self.assertTrue("File not found." in str(context.exception))

    def test_fileExists_FileFound_ReturnsTrue(self):
        file = open(self.FILE_PATH, "x")
        file.close()

        result: bool = self.configuration.file_exists(self.FILE_PATH)

        self.assertTrue(result)

    def test_readJson_InvalidJson_RaisesException(self):
        file = open(self.FILE_PATH, "w")
        file.write(self.INVALID_JSON_STRING)
        file.close()

        with self.assertRaises(json.JSONDecodeError) as context:
            self.configuration.read_json(self.FILE_PATH)
        
        self.assertEqual(context.exception.msg, "Expecting ':' delimiter")

    def test_readJson_ValidJson_ReturnsDict(self):
        file = open(self.FILE_PATH, "w")
        file.write(self.VALID_JSON_STRING)
        file.close()
        
        result = self.configuration.read_json(self.FILE_PATH)
        
        self.assertIsInstance(result, dict)
        self.assertEqual(result, self.VALID_JSON)
        

if __name__ == '__main__':
    unittest.main()
