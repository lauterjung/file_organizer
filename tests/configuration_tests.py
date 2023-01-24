import os
import shutil
import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path('src/').resolve()))

from src.exceptions.FileNotFound import FileNotFound
from src.model.Configuration import Configuration

class ConfigurationTests(unittest.TestCase):
    TEST_FOLDER_PATH: str = "tests/test_folder"
    configuration: Configuration

    def setUp(self) -> None:
        if not os.path.exists(self.TEST_FOLDER_PATH):
            os.mkdir(self.TEST_FOLDER_PATH, mode=2)

        self.configuration = Configuration()

    def tearDown(self) -> None:
        if os.path.exists(self.TEST_FOLDER_PATH):
            shutil.rmtree(self.TEST_FOLDER_PATH, ignore_errors=True)
    
    def test_fileExists_FileNotFound_RaisesException(self):
        file_path: str = ""

        with self.assertRaises(Exception) as context:
            self.configuration.file_exists(file_path)

        self.assertTrue("File not found." in str(context.exception))

    def test_fileExists_FileFound_ReturnsTrue(self):
        file_name: str = "app_config.json"
        file_path: str = self.TEST_FOLDER_PATH + "/" + file_name
        file = open(file_path, "x")
        file.close()
        
        result: bool = self.configuration.file_exists(file_path)

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
