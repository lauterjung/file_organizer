import unittest


class GeneralTests(unittest.TestCase):
    # config file
    def test_ReadConfigFile_FileDoesNotExists_RaisesException(self):
        self.assertTrue(False)
        
    def test_ReadConfigFile_InvalidJSON_RaisesException(self):
        self.assertTrue(False)
        
    def test_ReadConfigFile_InvalidOriginRootFolder_RaisesException(self):
        self.assertTrue(False)
        
    def test_ReadConfigFile_InvalidDestinyRootFolder_RaisesException(self):
        self.assertTrue(False)
        
    def test_ReadConfigFile_InvalidFileTypes_RaisesException(self):
        self.assertTrue(False)
        
    def test_ReadConfigFile_InvalidMatchPatterns_RaisesException(self):
        self.assertTrue(False)
        
    def test_ReadConfigFile_FileOk_ReturnsConfigObject(self):
        self.assertTrue(False)
        
    # origin folder
    def test_OriginRootFolder_FolderNotFound_RaisesException(self):
        self.assertTrue(False)
        
    def test_OriginRootFolder_FolderFound__(self):
        self.assertTrue(False)
        
    # destiny folder
    def test_DestinyRootFolder_FolderNotFound_RaisesException(self):
        self.assertTrue(False)
        
    def test_DestinyRootFolder_FolderFound__(self):
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