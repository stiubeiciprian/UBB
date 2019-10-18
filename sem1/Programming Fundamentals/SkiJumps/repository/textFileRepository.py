from domain.jump import Jump
from repository.repository import Repository


class TextFileRepository(Repository):

    def __init__(self, fileName):
        Repository.__init__(self)
        self.__fileName = fileName
        self.loadFromFile()

    def loadFromFile(self):
        """
        Function that loads elements from text file in to memory repository.
        """

        file = open(self.__fileName, "r")

        line = file.readline().strip()
        while line != "":
            line = line.split(",")
            jump = Jump(line[0], float(line[1]), float(line[2]),float(line[3]))
            Repository.add(self, jump)
            line = file.readline()

        file.close()

    def getAll(self):
        return Repository.getAll(self)