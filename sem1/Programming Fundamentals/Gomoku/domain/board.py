from texttable import Texttable
from domain.square import Square


class GameBoard(object):
    """
    Class that represents a game board.
        size - width / length of the game board
    """

    def __init__(self, repo):
        self.__repo = repo

    def makeMove(self, sq):
        """
        Places a player piece on the given square.
        :param sq: - square
        :return: -
        """

        self.__repo.add(sq)

    def isWin(self, sq):
        """
        Checks if the last placed piece determines a win.
        :para sq: - square of the latest placed piece
        :return: True - if game is won by a player
                 False - otherwise
        """
        directions = [[1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, -1], [-1, 0]]

        for direction in directions:
            length = 1

            newX = sq.getX() + direction[0]
            newY = sq.getY() + direction[1]
            player = sq.getPlayer()
            newSq = Square(newX, newY, None)
            newSq = self.__repo.search(newSq)

            while newSq != -1 and newSq.getPlayer() == player and length < 5:
                length += 1
                newX += direction[0]
                newY += direction[1]
                newSq = Square(newX, newY, None)
                newSq = self.__repo.search(newSq)

            if length == 5:
                return True

        return False

    def getMoves(self):
        """
        Function that returns all moves from the game board.
        :return: list of moves, [sq1, sq2, ..., sqn] where sq1, sq2, ..., sqn are Squares
        """
        return self.__repo.getAll()

    def isTie(self):
        """
        Function that determines if the game ended in a tie.
        :return: True, if the game is tied
                 False, if the game is not tied
        """
        if len(self.__repo.getAll()) == 15*15:
            return True
        return False

    def clearBoard(self):
        """
        Function that clears the board.
        """
        self.__repo.removeAll()

    def __str__(self):
        """
        Function that creates a string representation of the game board.
        :return: string of characters
        """
        t = Texttable()

        for i in range(1, 16):
            lst = []
            for j in range(1, 16):
                sq = self.__repo.search(Square(i, j, None))
                if sq == -1:
                    lst.append(" ")
                else:
                    lst.append(str(sq))
            t.add_row(lst)
        return t.draw()
