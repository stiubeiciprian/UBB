from errors.errors import UndoError


class UndoController(object):
    def __init__(self):
        self.__pos = -1
        self.__operations = []
        self.__fromUndo = False

    def add(self, operation):

        if self.__fromUndo:
            return

        self.__pos += 1
        self.__operations = self.__operations[:self.__pos]
        self.__operations.append(operation)

    def undo(self):
        if self.__pos == -1:
            raise UndoError("No more undos!")

        self.__fromUndo = True

        self.__operations[self.__pos].undo()

        self.__fromUndo = False
        self.__pos -= 1

    def redo(self):
        if len(self.__operations) == 0:
            raise UndoError("No more redos!")

        if self.__pos >= len(self.__operations)-1:
            raise UndoError("No more redos!")

        self.__fromUndo = True

        self.__pos += 1
        self.__operations[self.__pos].redo()

        self.__fromUndo = False

