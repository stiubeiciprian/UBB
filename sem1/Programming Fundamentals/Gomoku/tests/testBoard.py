import unittest

from domain.board import GameBoard
from domain.square import Square
from repository.repository import Repository


class TestBoard(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_makeMove(self):

        repo = Repository()
        board = GameBoard(repo)

        board.makeMove(Square(1, 1, 1))
        self.assertEqual(repo.getAll(), [Square(1, 1, 1)])

        board.makeMove(Square(2, 2, 2))
        self.assertEqual(repo.getAll(), [Square(1, 1, 1), Square(2, 2, 2)])

    def test_isWin(self):

        repo = Repository()
        board = GameBoard(repo)

        repo.add(Square(1, 1, 1))
        self.assertFalse(board.isWin(Square(1, 1, 1)))

        for i in range(2, 6):
            repo.add(Square(i, i, 1))

        self.assertTrue(board.isWin(Square(5, 5, 1)))

    def test_isTie(self):

        repo = Repository()
        board = GameBoard(repo)

        self.assertFalse(board.isTie())

        repo2 = Repository()

        for i in range(1, 16):
            for j in range(1, 16):
                repo2.add(Square(i, j, 1))

        board2 = GameBoard(repo2)
        self.assertTrue(board2.isTie())

    def test_getMoves(self):

        repo = Repository()
        board = GameBoard(repo)

        repo.add(Square(1, 1, 1))

        self.assertEqual(board.getMoves(), repo.getAll())

    def test_clearBoard(self):

        repo = Repository()
        board = GameBoard(repo)

        repo.add(Square(1, 1, 1))
        repo.add(Square(2, 2, 2))

        board.clearBoard()

        self.assertEqual(board.getMoves(), [])









