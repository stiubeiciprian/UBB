class Student(object):

    def __init__(self, studentId, name):
        self.__studentId = studentId
        self.__name = name

    def __str__(self):
        return 'id: ' + str(self.__studentId) + ' name: ' + str(self.__name)

    def __eq__(self, other):
        if type(other) == int:
            return self.__studentId == other
        return self.__studentId == other.__studentId

    def getId(self):
        return self.__studentId

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName
