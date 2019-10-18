from errors.errors import RepoError, ValidError


class Console(object):

    def __init__(self, gameCont):
        self.__gameCont = gameCont

    @staticmethod
    def gameOver(gameStatus, player):
        if gameStatus == 1:
            print("Game won by ", player)
            print("To quit the game type: exit. If you want to play again make a new move.")
            return True

        if gameStatus == 2:
            print("Game tied.")
            print("To quit the game type: exit. If you want to play again make a new move.")
            return True

        return False

    def __uiMakeMove(self, param):
        if len(param) != 2:
            raise ValidError("Invalid input!\n Input format: m <x> <y>")

        gameStatus = self.__gameCont.movePlayer(int(param[0]), int(param[1]))

        if self.gameOver(gameStatus, "human player. "):
            return

        gameStatus = self.__gameCont.moveBot()

        if self.gameOver(gameStatus, "computer. "):
            return

        self.__uiPrintMoves()

    def __uiPrintMoves(self):

        print(str(self.__gameCont.getTable()))

    def run(self):

        commands = {
            'm': self.__uiMakeMove
        }

        while True:
            try:
                param = input(">>").strip().split()

                if param[0] in commands:
                    commands[param[0]](param[1:])
                elif param[0] == "p":
                    self.__uiPrintMoves()
                elif param[0] == "exit":
                    return
                else:
                    print("Invalid command!")

            except ValueError:
                print("Invalid input!")
            except RepoError as re:
                print(re)
            except ValidError as ve:
                print(ve)
