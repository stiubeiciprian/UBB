class FunctionCall:
    def __init__(self, functionRef, *parameters):
        self.__functionRef = functionRef
        self.__parameters = parameters

    def call(self):
        self.__functionRef(*self.__parameters)
