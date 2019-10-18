from errors.errors import ValidError


class DisciplineValidator(object):
    
    def __init__(self):
        pass

    @staticmethod
    def validate_discipline(disc):
        errors = ""

        if disc.getId() < 0:
            errors += "Discipline id can't be negative!\n"

        if len(disc.getName()) == 0:
            errors += "Discipline name can't be empty!\n"

        if len(errors) > 0:
            raise ValidError(errors)
