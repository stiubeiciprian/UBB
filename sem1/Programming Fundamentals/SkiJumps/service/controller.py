class Controller(object):

    def __init__(self, repo):
        self.__repo = repo

    def getAll(self):
        """
        Function that returns all elements from repository
        """
        return self.__repo.getAll()


    def getWinners(self):
        """
        Function that returns top 3 skiers sorted by distance.
        Input:-
        Output: list with the top 3 skiers
        """
        return sorted(self.__repo.getAll(), key= lambda x: x.getDistance(), reverse=True)[:3]

    def plot(self):
        """
        Function that writes in plot.txt
        :return:
        """
        file = open("plot2.txt", "w")

        accStar = 1

        for elem in sorted(self.__repo.getAll(), key= lambda x: x.getDistance()):
            while accStar < elem.getDistance():
                file.write("*")
                accStar+=1
            file.write(elem.getName())
            accStar = int(elem.getDistance())

        file.close()


