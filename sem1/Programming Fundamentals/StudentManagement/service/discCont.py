from model.discipline import Discipline
from model.functioncall import FunctionCall
from model.operation import Operation


class DisciplineController(object):

    def __init__(self, repo, valid, undoCont):
        self.__repo = repo
        self.__valid = valid
        self.__undoCont = undoCont

    def addDiscipline(self, discId, name):
        discipline = Discipline(discId, name)
        self.__valid.validate_discipline(discipline)

        undo = FunctionCall(self.remove, discipline.getId())
        redo = FunctionCall(self.addDiscipline, discipline.getId(), discipline.getName())

        operation = Operation(undo, redo)

        self.__repo.add(discipline)
        self.__undoCont.add(operation)

    def updateDisciplineName(self, discId, newname):
        discipline = self.__repo.search(discId)

        undo = FunctionCall(self.updateDisciplineName, discId, discipline.getName())

        newdiscipline = Discipline(discId, newname)

        redo = FunctionCall(self.updateDisciplineName, discId, newname)

        operation = Operation(undo, redo)

        self.__repo.update(newdiscipline)
        self.__undoCont.add(operation)

    def searchDisciplineId(self, discId):
        return self.__repo.search(discId)

    def searchDisciplineTitle(self, title):
        searchList = []
        title = title.lower()
        for elem in self.__repo.getAll():
            if title in elem.getName().lower():
                searchList.append(elem)

        return searchList

    def remove(self, discId):

        discipline = self.searchDisciplineId(discId)
        undo = FunctionCall(self.addDiscipline, discipline.getId(), discipline.getName())
        redo = FunctionCall(self.remove, discId)
        operation = Operation(undo, redo)

        self.__repo.remove(discId)
        self.__undoCont.add(operation)

    def getAll(self):
        return self.__repo.getAll()
