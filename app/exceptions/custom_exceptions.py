class UserNotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message


class HeaderMissingException(Exception):
    def __init__(self, message: str):
        self.message = message

class UnauthorizedUserException(Exception):
    def __init__(self, message: str):
        self.message = message

