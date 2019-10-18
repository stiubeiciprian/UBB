class Console(object):

    def __init__(self, gameController):
        self.__gameController = gameController

    def uiStartNewGame(self):

        self.__gameController.resetBoard()
        self.__gameController.placeStars()
        self.__gameController.placeUSSE()
        self.__gameController.placeBlingonShips(3)
        print(self.__gameController.getBoard())

    def uiCheat(self):

        print(self.__gameController.getCheatBoard())

    def uiWarp(self, coordinates):
        pass

    def uiFire(self, coordinates):
        pass



    def run(self):

        while True:
            try:
                command = input(">>")

                if command == "start":
                    self.uiStartNewGame()
                elif command == "cheat":
                    self.uiCheat()
                elif command[:5] == "warp ":
                    self.uiWarp(command[5:])
                elif command[:5] == "fire ":
                    self.uiFire(command[5:])
                elif command == "exit":
                    return
                else:
                    print("Invalid command!")
            except ValueError:
                print("Invalid input type!")