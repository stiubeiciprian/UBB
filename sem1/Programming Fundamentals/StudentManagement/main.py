from repository.picklerepo import RepositoryBinaryFile
from repository.textfilerepo import *

from service.studCont import *
from service.discCont import *
from service.gradeCont import *
from service.undoCont import UndoController

from validators.gradeValid import *
from validators.studentValid import *
from validators.disciplineValid import *

from ui.console import *

settings = open("settings.properties", "r")

line = settings.readline().strip()

if line[2] == "inmemory":
    studRepo = Repository()
    discRepo = Repository()
    gradeRepo = Repository()
elif line[2] == "textfile":
    studRepo = RepositoryTextFileStudent("students.txt")
    discRepo = RepositoryTextFileDiscipline("disciplines.txt")
    gradeRepo = RepositoryTextFileGrade("grades.txt")
else:
    studRepo = RepositoryBinaryFile("students.pickle")
    discRepo = RepositoryBinaryFile("disciplines.pickle")
    gradeRepo = RepositoryBinaryFile("grades.pickle")

settings.close()


studValid = StudentValidator()
discValid = DisciplineValidator()
gradeValid = GradeValidator()

undoCont = UndoController()
studCont = StudentController(studRepo, studValid, undoCont)
discCont = DisciplineController(discRepo, discValid, undoCont)
gradeCont = GradeController(gradeRepo, studRepo, discRepo, gradeValid, undoCont)

ui = Console(discCont, studCont, gradeCont, undoCont)

ui.run()
