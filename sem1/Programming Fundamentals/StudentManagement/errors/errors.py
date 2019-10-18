class RepoError(Exception):
    def __init__(self, errors):
        self.__errors = errors

    def __str__(self):
        return self.__errors


class ValidError(Exception):
    
    def __init__(self, errors):
        self.__errors = errors

    def __str__(self):
        return self.__errors


class UndoError(Exception):

    def __init__(self, errors):
        self.__errors = errors

    def __str__(self):
        return self.__errors
