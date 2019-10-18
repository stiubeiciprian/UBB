import unittest
from domain.square import *


class TestSquare(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_getters(self):

        sq = Square(1, 1, 1)

        self.assertEqual(sq.getX(), 1)
        self.assertEqual(sq.getY(), 1)
        self.assertEqual(sq.getPlayer(), 1)

    def test_str(self):

        sq1 = Square(1, 1, 1)
        sq2 = Square(2, 2, 2)

        self.assertEqual(str(sq1), "X")
        self.assertEqual(str(sq2), "Y")

    def test_equ(self):
        sq1 = Square(1, 1, 1)
        sq2 = Square(2, 2, 2)
        sq3 = Square(1, 1, 3)

        self.assertTrue(sq1 == sq3)
        self.assertFalse(sq1 == sq2)
