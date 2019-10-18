from errors.errors import ValidError


class GradeValidator(object):

    def __init__(self):
        pass

    @staticmethod
    def validate_grade(grade):
        errors = ""

        if grade.get_studentId() < 0:
            errors += "Student id can't be negative!\n"

        if grade.get_disciplineId() < 0:
            errors += "Grade id can't be negative!\n"

        if grade.get_gradeValue() < 0:
            errors += "Grade value can't be negative!\n"

        if grade.get_gradeValue() > 10:
            errors += "Grade value must be < 10!\n"

        if len(errors) > 0:
            raise ValidError(errors)
