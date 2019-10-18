from errors.errors import RepoError


class Repository(object):

    def __init__(self):
        self.__elems = []

    def __len__(self):
        return len(self.__elems)

    def add(self, elem):
        """
        Function that adds an element to the repository.
        :return: added element
                 -1 if error
        """

        if elem in self.__elems:
            raise RepoError("Element already exists!")

        self.__elems.append(elem)

        return elem

    def remove(self, elem):
        """
        Function that removes an element from the repository.
        :return: removed element
                 -1 if error
        """

        if elem not in self.__elems:
            raise RepoError("Inexisting element!")

        for i in range(len(self.__elems)):
            if self.__elems[i] == elem:
                elem = self.__elems[i]
                del self.__elems[i]
                return elem

        return -1

    def search(self, elem):
        """
        Function that searches for given element in the repository.
        :return: searched elem
                 -1 if element is not found
        """
        for e in self.__elems:
            if e == elem:
                return e

        return -1

    def getAll(self):
        """
        Function that returns all elements from the repository.
        :return: list of all elements
        """
        return self.__elems

    def removeAll(self):
        """
        Function that removes all elements from the repository.
        """
        self.__elems = []
