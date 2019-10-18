import unittest

from domain.jump import Jump
from repository.repository import Repository
from repository.textFileRepository import TextFileRepository
from service.controller import Controller


class TestRepository(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_repo(self):

        repo = Repository()

        assert repo.getAll() == []

        jump1 = Jump("Gregor",32.47,12,-3)
        jump2 = Jump("Iane", 43.42, 10, 3)

        repo.add(jump1)

        assert repo.getAll() == [jump1]

        repo.add(jump2)

        assert repo.getAll() == [jump1, jump2]


class TestTextFileRepository(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_textfile(self):

        repo = TextFileRepository("test_text_file.txt")
        assert len(repo.getAll()) == 2

        repo = TextFileRepository("test_text_file2.txt")
        assert len(repo.getAll()) == 3

class TestController(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_controller(self):

        repo = TextFileRepository("test_jumps.txt")
        cont = Controller(repo)

        assert cont.getAll() == repo.getAll()

        assert cont.getWinners() == sorted(repo.getAll(), key= lambda x: x.getDistance(), reverse=True)[:3]