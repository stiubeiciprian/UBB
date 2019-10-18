from model.cascadedoperation import CascadeOperation
from model.functioncall import FunctionCall
from model.grade import Grade
from model.operation import Operation


class GradeController(object):
    def __init__(self, gradeRepo, studRepo, discRepo, valid, undoCont):
        self.__gradeRepo = gradeRepo
        self.__studRepo = studRepo
        self.__discRepo = discRepo
        self.__valid = valid
        self.__undoCont = undoCont

    def addGrade(self, discId, studId, value):
        grade = Grade(discId, studId, value)
        self.__valid.validate_grade(grade)

        undo = FunctionCall(self.remove, grade.getId())
        redo = FunctionCall(self.addGrade, discId, studId, value)

        operation = Operation(undo, redo)

        self.__gradeRepo.add(grade)
        self.__undoCont.add(operation)

        return grade

    def remove(self, gradeId):
        grade = self.__gradeRepo.search(gradeId)
        undo = FunctionCall(self.addGrade, grade.get_disciplineId(), grade.get_studentId(), grade.get_gradeValue())
        redo = FunctionCall(self.remove, gradeId)
        operation = Operation(undo, redo)
        self.__gradeRepo.remove(gradeId)
        self.__undoCont.add(operation)

    def getAll(self):
        return self.__gradeRepo.getAll()

    def removeByStudentId(self, studId):

        cascade = CascadeOperation()

        undo = FunctionCall(self.__studRepo.add, self.__studRepo.search(studId))
        redo = FunctionCall(self.__studRepo.remove, studId)
        operation = Operation(undo, redo)
        cascade.add(operation)

        self.__studRepo.remove(studId)

        for elem in self.getAll():
            if elem.get_studentId() == studId:
                undo = FunctionCall(self.addGrade, elem.get_disciplineId(), elem.get_studentId(), elem.get_gradeValue())
                redo = FunctionCall(self.remove, elem.getId())

                operation = Operation(undo, redo)
                cascade.add(operation)

                self.remove(elem.getId())

        self.__undoCont.add(cascade)

    def removeByDisciplineId(self, discId):

        cascade = CascadeOperation()

        discipline = self.__discRepo.search(discId)

        undo = FunctionCall(self.__discRepo.add, discipline.getId(), discipline.getName())
        redo = FunctionCall(self.__discRepo.remove, discId)
        operation = Operation(undo, redo)
        cascade.add(operation)

        self.__discRepo.remove(discId)

        for elem in self.getAll():
            if elem.get_disciplineId() == discId:
                undo = FunctionCall(self.addGrade, discId, elem.get_studentId(), elem.get_gradeValue())
                redo = FunctionCall(self.remove, elem.getId())

                operation = Operation(undo, redo)

                cascade.add(operation)

                self.remove(elem.getId())

        self.__undoCont.add(cascade)

    def __getAvgStud(self, student):
        sum = 0
        nr = 0

        for elem in self.__gradeRepo.getAll():
            if elem.get_studentId() == student:
                sum += elem.get_gradeValue()
                nr += 1

        return sum/nr

    def getStudentAtDisc(self, disc, sortCrt):
        lst = []
        for elem in self.__gradeRepo.getAll():
            if elem.get_disciplineId() == disc:
                if elem.get_studentId() not in lst:
                    lst.append(self.__studRepo.search(elem.get_studentId()))

        if sortCrt == 'avg':
            return sorted(lst, key=lambda x: self.__getAvgStud(x), reverse=True)

        elif sortCrt == 'alpha':
            return sorted(lst, key=lambda x: x.getName())

    def __getAvgAtDisc(self, student, disc):

        pass

    def __getStudentGrades(self, student):

        gradeList = []

        for elem in self.__gradeRepo.getAll():
            if elem.get_studentId() == student:
                gradeList.append(elem)

        return gradeList
