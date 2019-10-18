import pickle

from errors.errors import RepoError
from repository.repository import Repository


class RepositoryBinaryFile(Repository):

    def __init__(self, fileName):

        Repository.__init__(self)
        self.__fileName = fileName
        self.loadFromFile()

    def loadFromFile(self):
        """"
        Load data from file.
        raise FileError if there is an error
        """
        try:
            file = open(self.__fileName, "rb")
            content = pickle.load(file)
        except EOFError:
            content = []
        except IOError:
            raise RepoError("File error!")

        for elem in content:
            Repository.add(self, elem)

        file.close()

    def saveToFile(self):
        """
        Store data to file.
        """

        file = open(self.__fileName, "wb")

        content = Repository.getAll(self)

        pickle.dump(content, file)

        file.close()

    def add(self, elem):
        """
        Function that adds an element to the repository.
        Input: elem
        Output: -
        Raise: RepoError - if elem does already exist
        """
        Repository.add(self, elem)
        self.saveToFile()

    def update(self, elem):
        """
        Function that updates an element in the repository.
        Input: elem
        Output: -
        Raise: RepoError - if elem does not exist
        """
        Repository.update(self, elem)
        self.saveToFile()

    def remove(self, elem):
        """
        Function that removes an element from the repository.
        Input: elem
        Output: -
        Post: elem is deleted from repository
        Raise: RepoError - if elem does not exist
        """
        Repository.remove(self, elem)
        self.saveToFile()

    def removeAll(self):
        Repository.removeAll(self)
        self.saveToFile()
