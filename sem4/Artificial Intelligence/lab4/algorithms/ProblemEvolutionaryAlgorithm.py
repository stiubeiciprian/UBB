# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:09:60 2020

@author: Stiubei Ciprian
"""
import random


class ProblemEvolutionaryAlgorithm():
    def __init__(self, n):
        self.n = n

    def __generatePermutation(self):
        x = [i for i in range(1, self.n + 1)]
        random.shuffle(x)
        
        return tuple(x)

    def createIndividual(self):
       return [self.__generatePermutation() for i in range(self.n * 2)]

    def createPopulation(self, size):
        return [self.createIndividual() for i in range(size)]
    
    def fitness(self, individual):
        score = 0
        sum = self.n * (self.n + 1) / 2

        for col in range(self.n):
           colSum1, colSum2 = 0, 0
           for row in range(self.n):
               colSum1 += individual[row][col]
               colSum2 += individual[row + self.n][col]

           score += 1 if colSum1 != sum else 0
           score += 1 if colSum2 != sum else 0

        for row in range(self.n):
            for col in range(self.n):
                for i in range(self.n):
                    for j in range(self.n):
                        if (row != i or col != j) and individual[row][col] == individual[i][j] and individual[row + self.n][col] == individual[i +self.n][j]:
                            score += 1

        return score

    def mutate(self, individual, p):
        if random.random() <= p:
            return individual
        
        mutatedIndividual = individual[:]
        mutation = self.__generatePermutation()
        componentIndex = random.randint(0, self.n * 2 - 1)
        
        mutatedIndividual[componentIndex] = mutation
        
        return mutatedIndividual

    def crossover(self, parent1, parent2):
        x = random.randint(0, len(parent1) - 1)
        y = random.randint(0, len(parent2) - 1)
        
        return parent1[:min(x,y)] + parent2[min(x,y):max(x,y)] + parent1[max(x,y):]

    def iteration(self, population, populationSize, p):
        halfSize = int(populationSize/2)
        for i in range(halfSize):
            child = self.crossover(population[i], population[i + halfSize])
            child = self.mutate(child, p)
            population.append(child)
            
        sortedPopulation = sorted(population, key=self.fitness)
        
        return sortedPopulation[:populationSize]
