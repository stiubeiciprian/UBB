from errors.errors import RepoError

class Repository(object):
    
    def __init__(self):
        self.__elems = []
    
    def add(self, elem):
        """
        Function that adds an element to the repository.
        Input: elem
        Output: -
        Raise: RepoError - if elem does already exist
        """
        if elem in self.__elems:
            raise RepoError("Element already exists!")
        self.__elems.append(elem)

    def getAll(self):
        """
        Function that returns all elements of the repository.
        In: -
        Out: repository_elements
        """
        return self.__elems[:]
