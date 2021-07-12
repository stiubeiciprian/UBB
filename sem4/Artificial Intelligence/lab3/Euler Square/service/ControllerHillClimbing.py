# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 19:09:49 2020

@author: Stiubei Ciprian
"""

class ControllerHillClimbing:
    def __init__(self, problem, maxIterations):
        self.problem = problem
        self.maxIterations = maxIterations
        
    def run(self):
        currentNode = self.problem.generateStartingPoint()
        currentIteration = 0
        
        while currentIteration < self.maxIterations:
            nextNode = self.problem.iteration(currentNode)
            
            if nextNode == currentNode:
                return currentNode, currentIteration
            
            currentIteration += 1
            currentNode = nextNode
            #print("Current node:", currentNode)
            #input(">> Pres enter for next iteration <<")
        
        return currentNode, currentIteration