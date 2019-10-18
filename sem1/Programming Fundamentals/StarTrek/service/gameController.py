import random
from copy import deepcopy

from texttable import Texttable

from Errors.gameError import GameError


class GameController(object):

    def __init__(self):
        self.__grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    def checkNeighbours(self, row, col, neighbours):
        # Check left side
        if row - 1 >= 0:
            if col - 1 >= 0:
                if self.__grid[row - 1][col - 1] in neighbours:
                    return True
            if col + 1 < 8:
                if self.__grid[row - 1][col + 1] in neighbours:
                    return True
            if self.__grid[row - 1][col] in neighbours:
                return True

        # Check right side
        if row + 1 < 8:
            if col - 1 >= 0:
                if self.__grid[row + 1][col - 1] in neighbours:
                    return True
            if col + 1 < 8:
                if self.__grid[row + 1][col + 1] in neighbours:
                    return True
            if self.__grid[row + 1][col] in neighbours:
                return True

        # Check centre
        if col - 1 >= 0:
            if self.__grid[row][col - 1] in neighbours:
                return True
        if col + 1 < 8:
            if self.__grid[row][col + 1] in neighbours:
                return True

        return False

    def placeStars(self):

        starsNo = 0

        while starsNo < 10:
            row = random.randrange(0, 8)
            col = random.randrange(0, 8)

            if self.__grid[row][col] == ' ' and self.checkNeighbours(row, col, ['*']) == False:
                self.__grid[row][col] = '*'
                starsNo += 1

    def placeUSSE(self):

        row = random.randrange(0, 8)
        col = random.randrange(0, 8)

        while self.__grid[row][col] == '*':
            row = random.randrange(0, 8)
            col = random.randrange(0, 8)

        self.__grid[row][col] = 'E'

    def placeBlingonShips(self, requestedNo):
        shipsNo = 0

        while shipsNo < requestedNo:
            row = random.randrange(0, 8)
            col = random.randrange(0, 8)

            if self.__grid[row][col] == ' ':
                self.__grid[row][col] = 'B'
                shipsNo += 1

    def warp(self, coord):
        """
        Change the current location of the ship to the given coordinates.
        :param coord: string representing coordinates of warp location (e.g. B4)
                      first character is a letter between A and H
                      second character is a digit between 1 and 8
        :return: True - if the warp happened
                 Flase - if the warp location is occupied by a Blingon Ship
        Raises GameError if a star is between the current location and the warp position.
        """
        pass

    def fire(self, coord, enemyShipsNo):

        self.translateCoordinates(coord)

        row = coord[0]
        col = coord[1]

        if self.checkNeighbours(row, col, ['E']) is False:
            raise GameError("No Blingon ship near the Endeavour!")

        for row in range(0, 7):
            for col in range(0, 7):
                if self.__grid[row][col] == 'B':
                    self.__grid[row][col] = ' '

        self.placeBlingonShips(enemyShipsNo - 1)


    def getBoard(self):
        board = Texttable()
        board.header([0, 1, 2, 3, 4, 5, 6, 7, 8])
        rowIndex = [['A'], ['B'], ['C'], ['D'], ['E'], ['F'], ['G'], ['H']]

        newGrid = deepcopy(self.__grid)

        for row in range(0,8):
            for col in range(0,8):
                if newGrid[row][col] == 'B':
                    if self.checkNeighbours(row, col, ['E']) is False:
                        newGrid[row][col] = ' '

        for row in range(0, 8):
            board.add_row(rowIndex[row] + newGrid[row])

        return board.draw()

    def getCheatBoard(self):
        board = Texttable()
        board.header([0, 1, 2, 3, 4, 5, 6, 7, 8])
        rowIndex = [['A'], ['B'], ['C'], ['D'],['E'], ['F'],  ['G'], ['H']]

        for row in range(0, 7):
            board.add_row(rowIndex[row] + self.__grid[row])

        return board.draw()

    def resetBoard(self):

        self.__grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    def setGrid(self, newGrid):
        self.__grid = newGrid

    def translateCoordinates(self, coord):

        rowTranslate = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        try:
            row = rowTranslate[coord[0]]
            col = int(coord[1]) - 1
        except:
            raise GameError("Invalid coordinates!")

        return [row, col]
