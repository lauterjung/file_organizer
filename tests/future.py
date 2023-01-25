import unittest


class GeneralTests(unittest.TestCase):        
    # origin folder
    def test_OriginRootFolder_FolderNotFound_RaisesException(self):
        self.assertTrue(False)
        
    def test_OriginRootFolder_FolderFound__(self):
        self.assertTrue(False)
        
    # destination folder
    def test_DestinationRootFolder_FolderNotFound_RaisesException(self):
        self.assertTrue(False)
        
    def test_DestinationRootFolder_FolderFound__(self):
        self.assertTrue(False)
        
    # files
    def test_CheckForFiles_FilesNotFound_RaisesException(self):
        self.assertTrue(False)
        
    def test_CheckForFiles_SingleFileFound_Returns1(self):
        result = check_for_files()
        self.assertEquals(1, result)
        
    def test_CheckForFiles_TwoFilesFound_Returns2(self):
        result = check_for_files()
        self.assertEquals(2, result)


if __name__ == '__main__':
    unittest.main()