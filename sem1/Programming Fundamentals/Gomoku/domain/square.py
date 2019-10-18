class Square(object):
    """
    Representation of a square.
        x - row
        y - column
        player - player id

    Two squares are equal if they have the same coordinates.
    """

    def __init__(self, x, y, player):
        self.__x = x
        self.__y = y
        self.__player = player

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getPlayer(self):
        return self.__player

    def __eq__(self, other):

        if type(self) != type(other):
            return False

        return self.getY() == other.getY() and self.getX() == other.getX()

    def __str__(self):

        if self.__player == 1:
            return "X"
        else:
            return "Y"
