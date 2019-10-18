import unittest

from Errors.gameError import GameError
from service.gameController import GameController


class TestWarp(unittest.TestCase):

    def test_warp(self):

        gameController = GameController()
        gameGrid = [
            [' ', '*', ' ', '*', ' ', ' ', '*', ' '],
            [' ', ' ', 'E', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
            ['*', ' ', ' ', ' ', ' ', '*', ' ', ' '],
            [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '*', ' ', ' ', 'B'],
            [' ', '*', ' ', 'B', ' ', ' ', ' ', '*'],
            [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ']
        ]

        gameController.setGrid(gameGrid)
        gameController.placeStars()
        gameController.placeUSSE()
        gameController.placeBlingonShips()

        # Warp -----------------------------------------------

        # horizontal
        self.assertTrue(gameController.warp("B4"))
        self.assertTrue(gameController.warp("B1"))

        # vertical
        self.assertTrue(gameController.warp("A1"))
        self.assertTrue(gameController.warp("C1"))

        # diagonal
        self.assertTrue(gameController.warp("D2"))
        self.assertTrue(gameController.warp("C3"))
        self.assertTrue(gameController.warp("B2"))
        self.assertTrue(gameController.warp("C1"))

        # Invalid coordinates ---------------------------------

        try:
            gameController.warp("B3")
        except GameError as ge:
            self.assertEqual(str(ge) == "Invalid move!")

        try:
            gameController.warp("O3")
        except GameError as ge:
            self.assertEqual(str(ge) == "Invalid coordinates!")

        try:
            gameController.warp("O312")
        except GameError as ge:
            self.assertEqual(str(ge) == "Invalid coordinates!")

        # Star is blocking the warp ---------------------------

        try:
            gameController.warp("D1")
        except GameError as ge:
            self.assertEqual(str(ge) == "Star is in the way!")

        try:
            gameController.warp("F1")
        except GameError as ge:
            self.assertEqual(str(ge) == "Star is in the way!")

        gameController.warp("F4")

        # Endeavour lands on Blingon ship -----------------------

        self.assertFalse(gameController.warp("G4"))
