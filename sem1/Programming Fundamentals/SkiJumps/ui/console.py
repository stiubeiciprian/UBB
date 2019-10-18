from errors.errors import RepoError


class Console(object):

    def __init__(self, cont):
        self.__cont = cont

    def __uiDetermineWinners(self):

        for elem in self.__cont.getWinners():
            print(elem)

    def __uiPlotJumps(self):
        self.__cont.plot()
        pass

    def __uiPrintAll(self):

        for elem in self.__cont.getAll():
            print(str(elem))

    def run(self):

        commands = {
            "win": self.__uiDetermineWinners,
            "plot": self.__uiPlotJumps,
            "print": self.__uiPrintAll
        }


        try:

            while True:
                cmd = input(">>")

                if cmd in commands:
                    commands[cmd]()
                elif cmd == "exit":
                    return
                else:
                    print("Invalid command!")

        except ValueError:
            print("Invalid input type!")

        except RepoError as re:
            print(re)

        except IOError:
            print("File error!")


