class Operation(object):
    def __init__(self, functionUndo, functionRedo):
        self.__functionUndo = functionUndo
        self.__functionRedo = functionRedo

    def undo(self):
        self.__functionUndo.call()

    def redo(self):
        self.__functionRedo.call()
