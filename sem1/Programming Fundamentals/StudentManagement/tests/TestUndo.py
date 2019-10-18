import unittest

from model.discipline import Discipline
from model.grade import Grade
from repository.repository import Repository
from service.discCont import DisciplineController
from service.gradeCont import GradeController
from service.undoCont import UndoController
from validators.disciplineValid import DisciplineValidator
from validators.gradeValid import GradeValidator


class TestUndo(unittest.TestCase):

    def test_undo_redo(self):

        discRepo = Repository()
        studRepo = Repository()
        gradeRepo = Repository()
        valid = GradeValidator()
        undoCont = UndoController()
        cont = GradeController(gradeRepo, studRepo, discRepo, valid, undoCont)
        discCont = DisciplineController(discRepo, DisciplineValidator(), undoCont)

        discList = [Discipline(1, "Algebra"),
                    Discipline(2, "Computational Logic"),
                    Discipline(3, "Fundamentals of Programming")
                    ]

        for elem in discList:
            discCont.addDiscipline(elem.getId(), elem.getName())

        grade1 = Grade(1, 1, 10)
        grade2 = Grade(2, 1, 9)
        grade3 = Grade(1, 2, 4)
        grade4 = Grade(2, 2, 5)

        gradeList = [
          grade1, grade2, grade3, grade4
        ]

        for elem in gradeList:
            elem = cont.addGrade(elem.get_disciplineId(), elem.get_studentId(), elem.get_gradeValue())

        undoCont.undo()

        undoCont.redo()





