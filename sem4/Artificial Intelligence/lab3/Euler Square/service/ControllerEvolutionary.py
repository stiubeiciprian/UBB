# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 19:09:49 2020

@author: Stiubei Ciprian
"""

class ControllerEvolutionary:
    def __init__(self, problem, populationSize, probability, maxIterations):
        self.problem = problem
        self.populationSize = populationSize
        self.maxIterations = maxIterations
        self.probability = probability
        
    def run(self):
        currentGeneration = self.problem.createPopulation(self.populationSize)
        currentIteration = 0
        
        while currentIteration < self.maxIterations:
            nextGeneration = self.problem.iteration(currentGeneration, self.populationSize, self.probability)
            currentIteration += 1
            currentGeneration = nextGeneration
        
        return currentGeneration, currentIteration