from errors.errors import RepoError
from repository.dataStruct import IterDataStruct


class Repository(object):

    def __init__(self):
        self.__elems = IterDataStruct()

    def add(self, elem):
        if elem in self.__elems:
            raise RepoError("Element already exists!")
        self.__elems.append(elem)

    def search(self, elem):
        if elem not in self.__elems:
            raise RepoError("Element does not exist!")
        for x in self.__elems:
            if x == elem:
                return x
                
    def update(self, elem):
        if elem not in self.__elems:
            raise RepoError("Element does not exist!")
        for i in range(len(self.__elems)):
            if self.__elems[i]==elem:
                self.__elems[i]=elem
                return

    def remove(self, elem):
        if elem not in self.__elems:
            raise RepoError("Element does not exist!")
        for i in range(len(self.__elems)):
            if self.__elems[i]==elem:
                del self.__elems[i]
                return

    def getAll(self):
        return self.__elems[:]

    def removeAll(self):
        self.__elems.clear()
