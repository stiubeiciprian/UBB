import unittest
from domain.square import *
from repository.repository import *


class TestRepository(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_add(self):
        repo = Repository()

        sq1 = Square(1, 1, 1)
        sq2 = Square(2, 2, 2)

        repo.add(sq1)
        repo.add(sq2)

        self.assertEqual(len(repo), 2)

        try:
            repo.add(sq1)
            self.assertEqual(True, False)
        except RepoError:
            self.assertEqual(True, True)

    def test_getAll(self):
        repo = Repository()

        sq1 = Square(1, 1, 1)
        sq2 = Square(2, 2, 2)

        repo.add(sq1)

        self.assertEqual([sq1], repo.getAll())

        repo.add(sq2)

        self.assertEqual([sq1,sq2], repo.getAll())

    def test_remove(self):
        repo = Repository()

        sq1 = Square(1, 1, 1)
        sq2 = Square(2, 2, 2)
        sq3 = Square(3, 3, 3)

        repo.add(sq1)
        repo.add(sq2)

        repo.remove(sq1)

        self.assertEqual([sq2], repo.getAll())

        try:
            repo.remove(sq3)
            self.assertEqual(True, False)
        except RepoError:
            self.assertEqual(True, True)

    def test_removeAll(self):
        repo = Repository()

        sq1 = Square(1, 1, 1)
        sq2 = Square(2, 2, 2)

        repo.add(sq1)
        repo.add(sq2)

        repo.removeAll()

        self.assertEqual(len(repo), 0)

    def test_search(self):
        repo = Repository()

        sq1 = Square(1, 1, 1)
        sq2 = Square(2, 2, 2)
        sq3 = Square(3, 3, 3)

        repo.add(sq1)
        repo.add(sq2)

        self.assertEqual(repo.search(sq3), -1)

        self.assertEqual(repo.search(sq2), sq2)
