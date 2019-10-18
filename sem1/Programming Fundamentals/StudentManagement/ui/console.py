from errors.errors import *


class Console(object):

    def __init__(self, discCont, studCont, gradeCont, undoCont):
        self.__discCont = discCont
        self.__studCont = studCont
        self.__gradeCont = gradeCont
        self.__undoCont = undoCont

    @staticmethod
    def __printList(lst):
        for elem in lst:
            print(str(elem))

    @staticmethod
    def __printMenu():
        string = '\nAvailable commands:\n'
        string += '\t list disc/stud/grade\n'
        string += '\t add disc/stud/grade\n'
        string += '\t remove disc/stud\n'
        string += '\t update disc title/stud name\n'
        string += '\t search disc title/stud name\n'
        string += '\t disc students avg/alpha\n'
        string += '\t exit\n'
        print(string)

    def __uiListDisc(self):
        self.__printList(self.__discCont.getAll())

    def __uiListStud(self):
        self.__printList(self.__studCont.getAll())

    def __uiListGrade(self):
        self.__printList(self.__gradeCont.getAll())

    def __uiAddDisc(self):
        discId = int(input("Enter discipline id:"))
        name = input("Enter discipline title:")
        self.__discCont.addDiscipline(discId, name)

    def __uiAddStud(self):
        studId = int(input("Enter student id:"))
        name = input("Enter student name:")
        self.__studCont.addStudent(studId, name)

    def __uiAddGrade(self):
        studId = int(input("Enter student id:"))
        discId = int(input("Enter discipline id:"))
        value = float(input("Enter grade:"))
        self.__gradeCont.addGrade(discId, studId, value)

    def __uiRemoveDisc(self):
        discId = int(input("Enter discipline id:"))
        self.__gradeCont.removeByDisciplineId(discId)

    def __uiRemoveStud(self):
        studId = int(input("Enter student id:"))
        self.__gradeCont.removeByStudentId(studId)

    def __uiUpdateDiscName(self):
        discId = int(input("Enter discipline id:"))
        newName = input("Enter new name:")
        self.__discCont.updateDisciplineName(discId, newName)

    def __uiUpdateStudName(self):
        studId = int(input("Enter student id:"))
        newName = input("Enter new name:")
        self.__studCont.updateStudentName(studId, newName)

    def __uiSearchStudName(self):
        name = input("Enter student name:")
        self.__printList(self.__studCont.searchStudentName(name))

    def __uiSearchStudId(self):
        studId = int(input("Enter student id:"))
        print(str((self.__studCont.searchStudentId(studId))))

    def __uiSearchDiscTitle(self):
        title = input("Enter discipline title:")
        self.__printList(self.__discCont.searchDisciplineTitle(title))

    def __uiSearchDiscId(self):
        discId = int(input("Enter discipline id:"))
        print(str((self.__discCont.searchDisciplineId(discId))))

    def __uiDisciplineStudentsAlpha(self):
        disc = int(input("Enter disc id:"))
        lst = self.__gradeCont.getStudentAtDisc(disc, 'alpha')
        self.__printList(lst)

    def __uiDisciplineStudentsAvg(self):
        disc = int(input("Enter disc id:"))
        lst = self.__gradeCont.getStudentAtDisc(disc, 'avg')
        self.__printList(lst)

    def __uiUndo(self):
        self.__undoCont.undo()

    def __uiRedo(self):
        self.__undoCont.redo()

    def run(self):
        commands = {
            'list disc': self.__uiListDisc,
            'list stud': self.__uiListStud,
            'list grade': self.__uiListGrade,
            'add disc': self.__uiAddDisc,
            'add stud': self.__uiAddStud,
            'add grade': self.__uiAddGrade,
            'remove disc': self.__uiRemoveDisc,
            'remove stud': self.__uiRemoveStud,
            'update disc title': self.__uiUpdateDiscName,
            'update stud name': self.__uiUpdateStudName,
            'search disc id': self.__uiSearchDiscId,
            'search disc title': self.__uiSearchDiscTitle,
            'search stud id': self.__uiSearchStudId,
            'search stud name': self.__uiSearchStudName,
            'disc students alpha': self.__uiDisciplineStudentsAlpha,
            'disc students avg': self.__uiDisciplineStudentsAvg,
            'undo': self.__uiUndo,
            'redo': self.__uiRedo
        }
        while True:
            try:
                self.__printMenu()
                command = input("Enter command: ")

                if command in commands:
                    commands[command]()

                elif command == 'exit':
                    return

            except ValueError:
                print("Invalid input value!")
            except RepoError as re:
                print("Repository error:")
                print(re)
            except ValidError as ve:
                print("Validation error:")
                print(ve)
            except UndoError as ue:
                print(ue)
