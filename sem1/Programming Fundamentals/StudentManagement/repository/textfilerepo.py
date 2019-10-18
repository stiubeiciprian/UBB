from errors.errors import RepoError
from model.discipline import Discipline
from model.grade import Grade
from model.student import Student
from repository.repository import Repository


class RepositoryTextFileGrade(Repository):

    def __init__(self, fileName):

        Repository.__init__(self)
        self.__fileName = fileName
        self.loadFromFile()

    def loadFromFile(self):
        """"
        Load data from file.
        raise FileError if there is an error
        """
        try:
            file = open(self.__fileName, "r")
        except IOError:
            RepoError("File error!")

        line = file.readline().strip()
        while line != "":
            params = line.split(";")
            grade = Grade(int(params[0]), int(params[1]), float(params[2]), params[4], params[3])
            Repository.add(self, grade)
            line = file.readline().strip()

        file.close()

    def saveToFile(self):
        """
        Store data to file.
        """

        file = open(self.__fileName, "w")

        grades = Repository.getAll(self)

        for grade in grades:
            line = str(grade.get_disciplineId()) + ";" + str(grade.get_studentId()) + ";" + str(grade.get_gradeValue()) + ";" + str(grade.get_gradeDate()) + ";" + str(grade.getId()) + "\n"
            file.write(line)

        file.close()

    def add(self, elem):
        """
        Function that adds an element to the repository.
        Input: elem
        Output: -
        Raise: RepoError - if elem does already exist
        """
        Repository.add(self, elem)
        self.saveToFile()

    def update(self, elem):
        """
        Function that updates an element in the repository.
        Input: elem
        Output: -
        Raise: RepoError - if elem does not exist
        """
        Repository.update(self, elem)
        self.saveToFile()

    def remove(self, elem):
        """
        Function that removes an element from the repository.
        Input: elem
        Output: -
        Post: elem is deleted from repository
        Raise: RepoError - if elem does not exist
        """
        Repository.remove(self, elem)
        self.saveToFile()


class RepositoryTextFileDiscipline(Repository):

    def __init__(self, fileName):

        Repository.__init__(self)
        self.__fileName = fileName
        self.loadFromFile()

    def loadFromFile(self):
        """"
        Load data from file.
        raise FileError if there is an error
        """
        try:
            file = open(self.__fileName, "r")
        except IOError:
            RepoError("File error!")

        line = file.readline().strip()
        while line != "":
            params = line.split(";")
            discipline = Discipline(int(params[0]), params[1])
            Repository.add(self, discipline)
            line = file.readline().strip()

        file.close()

    def saveToFile(self):
        """
        Store data to file.
        """

        file = open(self.__fileName, "w")

        disciplines = Repository.getAll(self)

        for discipline in disciplines:
            line = str(discipline.getId()) + ";" + str(discipline.getName()) + "\n"
            file.write(line)

        file.close()

    def add(self, elem):
        """
        Function that adds an element to the repository.
        Input: elem
        Output: -
        Raise: RepoError - if elem does already exist
        """
        Repository.add(self, elem)
        self.saveToFile()

    def update(self, elem):
        """
        Function that updates an element in the repository.
        Input: elem
        Output: -
        Raise: RepoError - if elem does not exist
        """
        Repository.update(self, elem)
        self.saveToFile()

    def remove(self, elem):
        """
        Function that removes an element from the repository.
        Input: elem
        Output: -
        Post: elem is deleted from repository
        Raise: RepoError - if elem does not exist
        """
        Repository.remove(self, elem)
        self.saveToFile()


class RepositoryTextFileStudent(Repository):

    def __init__(self, fileName):

        Repository.__init__(self)
        self.__fileName = fileName
        self.loadFromFile()

    def loadFromFile(self):
        """"
        Load data from file.
        raise FileError if there is an error
        """
        try:
            file = open(self.__fileName, "r")
        except IOError:
            raise RepoError("File error!")

        line = file.readline().strip()
        while line != "":
            params = line.split(";")
            student = Student(int(params[0]), params[1])
            Repository.add(self, student)
            line = file.readline().strip()

        file.close()

    def saveToFile(self):
        """
        Store data to file.
        """

        file = open(self.__fileName, "w")

        students = Repository.getAll(self)

        for student in students:
            line = str(student.getId()) + ";" + str(student.getName()) + "\n"
            file.write(line)

        file.close()

    def add(self, elem):
        """
        Function that adds an element to the repository.
        Input: elem
        Output: -
        Raise: RepoError - if elem does already exist
        """
        Repository.add(self, elem)
        self.saveToFile()

    def update(self, elem):
        """
        Function that updates an element in the repository.
        Input: elem
        Output: -
        Raise: RepoError - if elem does not exist
        """
        Repository.update(self, elem)
        self.saveToFile()

    def remove(self, elem):
        """
        Function that removes an element from the repository.
        Input: elem
        Output: -
        Post: elem is deleted from repository
        Raise: RepoError - if elem does not exist
        """
        Repository.remove(self, elem)
        self.saveToFile()

