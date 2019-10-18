from model.functioncall import FunctionCall
from model.operation import Operation
from model.student import Student


class StudentController(object):

    def __init__(self, repo, valid, undoCont):
        self.__repo = repo
        self.__valid = valid
        self.__undoCont = undoCont

    def addStudent(self, studId, name):

        student = Student(studId, name)

        self.__valid.validate_student(student)

        undo = FunctionCall(self.remove, student)
        redo = FunctionCall(self.addStudent, studId, name)

        operation = Operation(undo, redo)

        self.__repo.add(student)
        self.__undoCont.add(operation)

        return student

    def updateStudentName(self, studId, newname):
        student = self.__repo.search(studId)

        undo = FunctionCall(self.updateStudentName, studId, student.getName())
        newstudent = Student(studId, newname)
        redo = FunctionCall(self.updateStudentName, studId, newname)
        operation = Operation(undo, redo)
        self.__repo.update(newstudent)
        self.__undoCont.add(operation)

    def searchStudentId(self, studId):
        return self.__repo.search(studId)

    def searchStudentName(self, name):
        searchList = []
        name = name.lower()
        for elem in self.__repo.getAll():
            if name in elem.getName().lower():
                searchList.append(elem)

        return searchList

    def remove(self, studId):
        student = self.searchStudentId(studId)

        undo = FunctionCall(self.addStudent, student.getId(), student.getName())
        redo = FunctionCall(self.remove, studId)

        operation = Operation(undo, redo)

        self.__repo.remove(studId)
        self.__undoCont.add(operation)

    def getAll(self):
        return self.__repo.getAll()
