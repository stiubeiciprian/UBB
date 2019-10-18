from errors.errors import ValidError


class SquareValidator(object):

    def __init__(self):
        self.__msg = ""

    def validateSq(self, sq):

        errors = ""
        err = False

        if sq.getX() < 1 or sq.getX() > 15:
            errors += "X coord must be between 1 and 15 \n"
            err = True

        if sq.getY() < 1 or sq.getY() > 15:
            errors += "Y coord must be between 1 and 15 \n"
            err = True

        if err:
            raise ValidError(errors)

