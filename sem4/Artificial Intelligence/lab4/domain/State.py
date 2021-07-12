class State:
    def __init__(self, values):
        self.values = values
        
    def setValues(self, newValues):
        self.values = newValues
        
    def getValues(self):
        return self.values
    
    def __str__(self):
        half = int(len(self.values) / 2)
        s = '\n'
        for i in range(half):
            s += str(self.values[i]) + '\t' + str(self.values[i+half]) + '\n'

        return s
    
    def __repr__(self):
        return repr(self.values)
