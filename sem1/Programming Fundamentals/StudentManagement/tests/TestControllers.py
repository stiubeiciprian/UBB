import unittest

from errors.errors import ValidError, UndoError
from model.grade import Grade
from repository.repository import *
from service.discCont import *
from service.gradeCont import *
from service.studCont import *
from service.undoCont import UndoController
from validators.disciplineValid import DisciplineValidator
from validators.gradeValid import GradeValidator
from validators.studentValid import StudentValidator


class TestDisciplineController(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_addDiscipline(self):
        repo = Repository()
        valid = DisciplineValidator()
        undoCont = UndoController()
        cont = DisciplineController(repo, valid, undoCont)

        disc1 = Discipline(1, "Algebra")
        disc2 = Discipline(2, "Computational Logic")
        disc3 = Discipline(3, "Fundamentals of Programming")

        cont.addDiscipline(1, "Algebra")

        self.assertEqual(repo.getAll(), [disc1])

        cont.addDiscipline(2, "Computational Logic")
        self.assertEqual(repo.getAll(), [disc1, disc2])
        cont.addDiscipline(3, "Fundamentals of Programming")
        self.assertEqual(repo.getAll(), [disc1, disc2, disc3])

    def test_updateDisciplineName(self):
        repo = Repository()
        valid = DisciplineValidator()
        undoCont = UndoController()
        cont = DisciplineController(repo, valid, undoCont)

        disc1 = Discipline(1, "Algebra")
        disc2 = Discipline(2, "Computational Logic")
        disc3 = Discipline(3, "Fundamentals of Programming")

        cont.addDiscipline(1, "Algebra")
        cont.addDiscipline(2, "Computational Logic")
        cont.addDiscipline(3, "Fundamentals of Programming")

        cont.updateDisciplineName(1, "Analysis")

        assert repo.search(1).getName() == "Analysis"

        try:
            disc = Discipline(1001, "WWW")
            name = "CSA"
            cont.updateDisciplineName(disc, name)
            assert False
        except RepoError:
            pass

    def test_searchDisciplineId(self):
        repo = Repository()
        valid = DisciplineValidator()
        undoCont = UndoController()
        cont = DisciplineController(repo, valid, undoCont)

        disc1 = Discipline(1, "Algebra")
        disc2 = Discipline(2, "Computational Logic")
        disc3 = Discipline(3, "Fundamentals of Programming")

        cont.addDiscipline(1, "Algebra")
        cont.addDiscipline(2, "Computational Logic")
        cont.addDiscipline(3, "Fundamentals of Programming")

        self.assertEqual(cont.searchDisciplineId(1), disc1)
        self.assertEqual(cont.searchDisciplineId(2), disc2)
        self.assertEqual(cont.searchDisciplineId(3), disc3)

    def test_remove(self):
        repo = Repository()
        valid = DisciplineValidator()
        undoCont = UndoController()
        cont = DisciplineController(repo, valid, undoCont)

        disc1 = Discipline(1, "Algebra")
        disc2 = Discipline(2, "Computational Logic")
        disc3 = Discipline(3, "Fundamentals of Programming")

        cont.addDiscipline(1, "Algebra")
        cont.addDiscipline(2, "Computational Logic")
        cont.addDiscipline(3, "Fundamentals of Programming")

        cont.remove(2)
        self.assertEqual(cont.getAll(), [disc1, disc3])

        try:
            cont.remove(10)
            assert False
        except RepoError:
            pass

    def test_getAll(self):
        repo = Repository()
        valid = DisciplineValidator()
        undoCont = UndoController()
        cont = DisciplineController(repo, valid, undoCont)

        disc1 = Discipline(1, "Algebra")
        disc2 = Discipline(2, "Computational Logic")
        disc3 = Discipline(3, "Fundamentals of Programming")

        cont.addDiscipline(1, "Algebra")
        cont.addDiscipline(2, "Computational Logic")
        cont.addDiscipline(3, "Fundamentals of Programming")

        self.assertEqual(repo.getAll(), cont.getAll())


class TestStudentController(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_addStudent(self):

        repo = Repository()
        valid = StudentValidator()
        undoCont = UndoController()
        cont = StudentController(repo, valid, undoCont)

        assert repo.getAll() == []

        student = Student(1, "Winston")
        cont.addStudent(1, "Winston")
        assert repo.getAll() == [student]

        student2 = Student(2, "Smith")
        cont.addStudent(2, "Smith")
        assert repo.getAll() == [student, student2]

        try:
            student = Student(-1, "")
            cont.addStudent(-1, "")
            assert False
        except ValidError:
            pass

    def test_updateStudentName(self):
        repo = Repository()
        valid = StudentValidator()
        undoCont = UndoController()
        cont = StudentController(repo, valid, undoCont)

        student1 = Student(1, "Winsotn")
        student2 = Student(2, "Smith")
        student3 = Student(3, "Churchill")

        cont.addStudent(1, "Winsotn")
        cont.addStudent(2, "Smith")
        cont.addStudent(3, "Churchill")

        cont.updateStudentName(1, "Doe")

        assert repo.search(1).getName() == "Doe"

        try:
            student = Student(1001, "WWW")
            name = "John"
            cont.updateStudentName(student, name)
            assert False
        except RepoError:
            pass

    def test_searchStudentId(self):
        repo = Repository()
        valid = StudentValidator()
        undoCont = UndoController()
        cont = StudentController(repo, valid, undoCont)

        student1 = Student(1, "Winsotn")
        student2 = Student(2, "Smith")
        student3 = Student(3, "Churchill")

        cont.addStudent(1, "Winsotn")
        cont.addStudent(2, "Smith")
        cont.addStudent(3, "Churchill")

        assert cont.searchStudentId(1) == student1
        assert cont.searchStudentId(2) == student2
        assert cont.searchStudentId(3) == student3

    def test_searchStudentName(self):
        repo = Repository()
        valid = StudentValidator()
        undoCont = UndoController()
        cont = StudentController(repo, valid, undoCont)

        student1 = Student(1, "Winsotn")
        student2 = Student(2, "Smith")
        student3 = Student(3, "Churchill")

        cont.addStudent(1, "Winsotn")
        cont.addStudent(2, "Smith")
        cont.addStudent(3, "Churchill")

        assert cont.searchStudentName("i") == [student1, student2, student3]
        assert cont.searchStudentName("win") == [student1]
        assert cont.searchStudentName("Smith") == [student2]
        assert cont.searchStudentName("awd") == []

    def test_remove(self):
        repo = Repository()
        valid = StudentValidator()
        undoCont = UndoController()
        cont = StudentController(repo, valid, undoCont)

        student1 = Student(1, "Winsotn")
        student2 = Student(2, "Smith")
        student3 = Student(3, "Churchill")

        cont.addStudent(1, "Winsotn")
        cont.addStudent(2, "Smith")
        cont.addStudent(3, "Churchill")

        cont.remove(2)
        assert cont.getAll() == [student1, student3]

        try:
            cont.remove(10)
            assert False
        except RepoError:
            pass

        undoCont.undo()

        assert cont.getAll() == [student1, student3, student2]

        undoCont.redo()

        assert cont.getAll() == [student1, student3]

        undoCont.undo()
        undoCont.undo()
        undoCont.undo()
        undoCont.undo()

        try:
            undoCont.undo()
            assert False
        except UndoError:
            pass

    def test_getAll(self):

        repo = Repository()
        valid = StudentValidator()
        undoCont = UndoController()
        cont = StudentController(repo, valid, undoCont)

        student1 = Student(1, "Winsotn")
        student2 = Student(2, "Smith")
        student3 = Student(3, "Churchill")

        cont.addStudent(1, "Winsotn")
        cont.addStudent(2, "Smith")
        cont.addStudent(3, "Churchill")

        self.assertEqual(repo.getAll(), cont.getAll())


class TestGradeController(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_addGrade(self):
        discRepo = Repository()
        studRepo = Repository()
        gradeRepo = Repository()
        valid = GradeValidator()
        undoCont = UndoController()
        cont = GradeController(gradeRepo, studRepo,  discRepo, valid, undoCont)

        grade1 = cont.addGrade(1, 1, 10)




        self.assertEqual(gradeRepo.getAll(), [grade1])
        grade2 = cont.addGrade(2, 2, 10)
        self.assertEqual(gradeRepo.getAll(), [grade1, grade2])

        try:
            cont.addGrade(-1, -1, 100)
            self.assertTrue(False)
        except ValidError:
            pass

    def test_getAll(self):
        discRepo = Repository()
        studRepo = Repository()
        gradeRepo = Repository()
        valid = GradeValidator()
        undoCont = UndoController()
        cont = GradeController(gradeRepo, studRepo, discRepo, valid, undoCont)

        grade1 = Grade(1, 1, 10)
        grade2 = Grade(2, 2, 10)

        cont.addGrade(1, 1, 10)
        cont.addGrade(2, 2, 10)

        self.assertEqual(len(cont.getAll()), 2)

    def test_remove(self):
        discRepo = Repository()
        studRepo = Repository()
        gradeRepo = Repository()
        valid = GradeValidator()
        undoCont = UndoController()
        cont = GradeController(gradeRepo, studRepo, discRepo, valid, undoCont)

        grade1 = Grade(1, 1, 10)
        grade2 = Grade(2, 2, 10)

        cont.addGrade(1, 1, 10)
        cont.addGrade(2, 2, 10)

        gradeId = grade1.getId()

        cont.remove(gradeId)

        self.assertEqual(gradeRepo.getAll(), [grade2])

    def test_removeByStudentId(self):
        discRepo = Repository()
        studRepo = Repository()
        gradeRepo = Repository()
        valid = GradeValidator()
        undoCont = UndoController()
        cont = GradeController(gradeRepo, studRepo, discRepo, valid, undoCont)

        grade1 = Grade(1, 1, 10)
        grade2 = Grade(2, 2, 10)

        stud1 = Student(1, "Student1")
        stud2 = Student(2, "Student2")
        studRepo.add(stud1)
        studRepo.add(stud2)

        cont.addGrade(1, 1, 10)
        cont.addGrade(2, 2, 10)

        cont.removeByStudentId(1)

        self.assertEqual(gradeRepo.getAll(), [grade2])

    def test_removeByDisciplineId(self):
        discRepo = Repository()
        studRepo = Repository()
        gradeRepo = Repository()
        valid = GradeValidator()
        undoCont = UndoController()
        cont = GradeController(gradeRepo, studRepo, discRepo, valid, undoCont)

        grade1 = Grade(1, 1, 9)
        grade2 = Grade(2, 2, 7)

        disc1 = Discipline(1, "Discipline 1")
        disc2 = Discipline(2, "Discipline 2")
        discRepo.add(disc1)
        discRepo.add(disc2)

        cont.addGrade(1, 1, 9)
        cont.addGrade(2, 2, 7)

        cont.removeByDisciplineId(2)

        assert len(gradeRepo.getAll()) == 1
