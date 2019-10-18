class Discipline(object):

    def __init__(self, disciplineId, name):
        self.__disciplineId = disciplineId
        self.__name = name

    def __str__(self):
        return 'id: ' + str(self.__disciplineId) + ' name: ' + str(self.__name)

    def __eq__(self, other):
        if type(other) == int:
            return self.__disciplineId == other
        return self.__disciplineId == other.__disciplineId

    def getId(self):
        return self.__disciplineId

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName
