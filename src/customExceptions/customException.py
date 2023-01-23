class CustomException(Exception):

    def __init__(self, message="Custom exception message"):
        self.message = message
        super().__init__(self.message)