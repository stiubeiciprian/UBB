# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:09:60 2020

@author: Stiubei Ciprian
"""

class State:
    def __init__(self):
        self.values = []
        
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