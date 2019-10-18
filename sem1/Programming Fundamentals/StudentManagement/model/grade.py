import datetime


class Grade(object):

    def __init__(self, disciplineId, studentId, gradeValue, gradeId=None, gradeDate=None):
        self.__disciplineId = disciplineId
        self.__studentId = studentId
        self.__gradeValue = gradeValue

        if gradeDate is None:
            self.__gradeDate = str(datetime.datetime.now())
        else:
            self.__gradeDate = gradeDate

        if gradeId is None:
            self.__gradeId = str(self.__studentId) + str(self.__disciplineId) + self.__gradeDate
        else:
            self.__gradeId = gradeId

    def __str__(self):
        return '   stud: ' + str(self.__studentId) \
               + ' disc: ' + str(self.__disciplineId) \
               + ' grade: ' + str(self.__gradeValue)
    
    def __eq__(self, other):
        if type(other) == str:
            return self.getId() == other
        return self.getId() == other.getId()

    def getId(self):
        return self.__gradeId

    def get_disciplineId(self):
        return self.__disciplineId

    def get_studentId(self):
        return self.__studentId

    def get_gradeValue(self):
        return self.__gradeValue

    def get_gradeDate(self):
        return self.__gradeDate
