class ValidError(Exception):
    """
    Validation error.
    """
    def __init__(self, errors):
        self.__errors = errors

    def __str__(self):
        return self.__errors


class RepoError(Exception):
    """
    Repository error.
    """
    def __init__(self, errors):
        self.__errors = errors

    def __str__(self):
        return self.__errors


class GameException(Exception):
    """
    Game exception.
    """
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return self.__msg
