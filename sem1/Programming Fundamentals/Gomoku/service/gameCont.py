from domain.square import Square
import random


class GameController(object):

    def __init__(self, board, squareValidator):
        self.__board = board
        self.__squareValidator = squareValidator

    def movePlayer(self, x, y):
        """
        Function that makes a new player move and returns the state of the game.
        :param param: param = [ x, y ], where x = square row, y = square column
        :return: 1, if the game is won
                 2, if the game is tied
                -1, if the game is not over
        """

        sq = Square(x, y, 1)
        self.__squareValidator.validateSq(sq)
        self.__board.makeMove(sq)

        if self.__board.isWin(sq):
            self.__board.clearBoard()
            return 1
        elif self.__board.isTie():
            self.__board.clearBoard()
            return 2

        return -1

    def randomMove(self):
        """
        Function that generates a random move.
        :return: square
        """

        x = random.randint(1, 15)
        y = random.randint(1, 15)

        sq = Square(x, y, 2)

        if sq in self.getMoves():
            return self.randomMove()

        return sq

    def planMove(self):
        """
        Function that analyses the current board state and determines the computer's next move.
        :return: square
        """
        pass



    def moveBot(self):
        """
            Function that makes a new computer move and returns the state of the game.
            :param param: param = [ x, y ], where x = square row, y = square column
            :return: 1, if the game is won
                     2, if the game is tied
                    -1, if the game is not over
        """
        sq = self.randomMove()
        self.__board.makeMove(sq)

        if self.__board.isWin(sq):
            self.__board.clearBoard()
            return 1
        elif self.__board.isTie():
            self.__board.clearBoard()
            return 2

        return -1

    def getMoves(self):
        """
        Function that returns all moves.
        """
        return self.__board.getMoves()

    def getTable(self):
        """
        Function that returns a string of characters representing the table.
        """
        return str(self.__board)
