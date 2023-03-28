class ValidationException(Exception):
    """Exception raised for errors in ValueObjects class objects."""

    def __init__(self, errorValue, message):
        self.errorValue = errorValue
        self.message = message + f' ERROR VALUE: {errorValue}'
        super().__init__(self.message)