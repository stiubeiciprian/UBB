# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:09:49 2020

@author: Stiubei Ciprian
"""
import random
import itertools

class ProblemHillClimbing:
    def __init__(self, n):
        self.n = n
    
    def __generatePermutation(self):
        x = [i for i in range(1, self.n + 1)]
        random.shuffle(x)
        
        return tuple(x)

    def generateStartingPoint(self):
        return [self.__generatePermutation() for i in range(self.n * 2)]
    
    def getNeighbours(self, node):
        neighbours = []
        permutations = list(itertools.permutations([i for i in range(1, self.n + 1)]))
        
        for i in range(len(permutations)):
            for pos in range(self.n * 2):
                neighbour = node[:]
                neighbour[pos] = permutations[i]
                neighbours.append(neighbour)
        
        return neighbours

    def weight(self, node):
        score = 0

        s = self.n * (self.n + 1) / 2

        for col in range(self.n):
            colSum1, colSum2 = 0, 0
            for row in range(self.n):
                colSum1 += node[row][col]
                colSum2 += node[row + self.n][col]

        score += 1 if colSum1 != s else 0
        score += 1 if colSum2 != s else 0

        for row in range(self.n):
            for col in range(self.n):
                for i in range(self.n):
                    for j in range(self.n):
                        if (row != i or col != j) and node[row][col] == node[i][j] and node[row + self.n][col] == node[i + self.n][j]:
                            score += 1

        return score
        
    def orderNodes(self, nodes):
        return sorted(nodes, key=self.weight)
    
    def iteration(self, currentNode):
        neighbours = self.getNeighbours(currentNode)
        sortedNeighbours = self.orderNodes(neighbours)
        nextNode = sortedNeighbours[0]
        
        if self.weight(nextNode) > self.weight(currentNode):
            return currentNode
        
        return nextNode
