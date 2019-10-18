class CascadeOperation(object):
    def __init__(self):
        self.__operation = []

    def add(self, elem):
        self.__operation.append(elem)

    def undo(self):
        for elem in self.__operation:
            elem.undo()

    def redo(self):
        for elem in self.__operation:
            elem.redo()