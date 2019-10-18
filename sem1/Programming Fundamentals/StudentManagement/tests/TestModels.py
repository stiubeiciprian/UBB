import unittest
from model.discipline import *
from model.grade import *
from model.student import *


class TestDiscipline(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_discipline(self):
        disc = Discipline(1, "Programming Fundamentals")

        assert disc.getName() == "Programming Fundamentals"
        assert disc.getId() == 1

        disc.setName("CSA")
        assert disc.getName() == "CSA"

        assert disc == 1

        disc2 = Discipline(1, "Bla")

        assert disc == disc2

        assert str(disc) == "id: 1 name: CSA"


class TestGrade(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_grade(self):
        grade = Grade(1,1,10)

        assert grade.getId() == "11" + grade.get_gradeDate()
        assert grade.get_disciplineId() == 1
        assert grade.get_studentId() == 1
        assert grade.get_gradeValue() == 10

        assert str(grade) == "   stud: 1 disc: 1 grade: 10"

        assert grade == "11" + grade.get_gradeDate()


class TestStudent(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_student(self):
        student = Student(1, "Winston")

        assert student.getId() == 1
        assert student.getName() == "Winston"

        student.setName("Smith")
        assert student.getName() == "Smith"

        assert student == 1

        student2 = Student(1, "Churchill")
        assert student == student2

        assert str(student) == "id: 1 name: Smith"
