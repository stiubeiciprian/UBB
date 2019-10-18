from errors.errors import ValidError


class StudentValidator(object):

    def __init__(self):
        pass

    @staticmethod
    def validate_student(student):
        errors = ""

        if student.getId() < 0:
            errors += "Student id can't be negative!\n"

        if student.getName() == "":
            errors += "Student name can't be empty!\n"

        if len(errors) > 0:
            raise ValidError(errors)
