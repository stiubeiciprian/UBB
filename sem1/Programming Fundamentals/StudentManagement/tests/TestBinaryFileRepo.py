import unittest

from model.student import Student
from repository.picklerepo import *


class TestTextFileRepo(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_repository_getAll(self):
        repo = RepositoryBinaryFile("test_binary_repo.pickle")
        repo.removeAll()

        assert len(repo.getAll()) == 0

        repo.removeAll()

    def test_repository_add(self):
        repo = RepositoryBinaryFile("test_binary_repo.pickle")

        repo.removeAll()

        stud1 = Student(1, "Winston")
        stud2 = Student(2, "Smith")
        stud3 = Student(3, "Churchill")

        repo.add(stud1)
        repo.add(stud2)
        repo.add(stud3)

        assert len(repo.getAll()) == 3

        assert repo.getAll() == [stud1, stud2, stud3]

        repo.removeAll()

    def test_repository_search(self):
        repo = RepositoryBinaryFile("test_binary_repo.pickle")
        repo.removeAll()

        stud1 = Student(1, "Winston")
        stud2 = Student(2, "Smith")
        stud3 = Student(1, "Churchill")

        repo.add(stud1)
        repo.add(stud2)

        assert repo.search(1) == stud1
        assert repo.search(stud3) == stud1

        repo.removeAll()

    def test_repository_update(self):
        repo = RepositoryBinaryFile("test_binary_repo.pickle")
        repo.removeAll()

        stud1 = Student(1, "Winston")
        stud2 = Student(2, "Smith")
        stud3 = Student(1, "Churchill")

        repo.add(stud1)
        repo.add(stud2)

        repo.update(stud3)

        assert repo.getAll() == [stud3, stud2]

        repo.removeAll()

    def test_repository_remove(self):
        repo = RepositoryBinaryFile("test_binary_repo.pickle")
        repo.removeAll()

        stud1 = Student(1, "Winston")
        stud2 = Student(2, "Smith")
        stud3 = Student(3, "Churchill")

        repo.add(stud1)
        repo.add(stud2)
        repo.add(stud3)

        repo.remove(2)
        repo.remove(stud3)
        assert len(repo.getAll()) == 1

        assert repo.getAll() == [stud1]

        repo.removeAll()
