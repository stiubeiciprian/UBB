from copy import deepcopy


class DCGraph:

    def __init__(self):
        self.__din = {}
        self.__dout = {}
        self.__dcost = {}

    def addVertex(self, vertex):
        """
        Add a vertex to the graph.
        :param vertex: vertex (int)
        :return:    True - if the vertex was added
                    False - if the vertex already existed
        """

        if self.isVertex(vertex):
            return False

        self.__din.update({vertex: []})
        self.__dout.update({vertex: []})

        return True

    def removeVertex(self, vertex):
        """
        Remove a vertex to the graph.
        :param vertex: vertex (int)
        :return:    True - if the vertex was removed
                    False - if the vertex did not exist
        """

        if not self.isVertex(vertex):
            return False

        for v in self.__din[vertex]:
            self.__dout[v].remove(vertex)

        for v in self.__dout[vertex]:
            self.__din[v].remove(vertex)

        self.__din.pop(vertex)
        self.__dout.pop(vertex)

        for edge in list(self.__dcost.keys()):
            if vertex in edge:
                del self.__dcost[edge]

        return True

    def isVertex(self, vertex):
        """
        Check if vertex exists.
        :param vertex: Vertex
        :return:    True - if the vertex exists
                    False - otherwise
        """

        return vertex in self.__dout.keys()

    def getInDeg(self, vertex):
        """
        Return the in degree of the given vertex.
        :param vertex: vertex (int)
        :return: in degree of vertex
        """

        return len(self.__din[vertex])

    def getOutDeg(self, vertex):
        """
        Return the out degree of the given vertex.
        :param vertex: vertex (int)
        :return: out degree of vertex
        """

        return len(self.__dout[vertex])

    def getVertexNo(self):
        """
        Gets the number of vertices.
        :return: number of vertices
        """

        return len(self.__din)

    def isEdge(self, source, target):
        """
        Check if the edge exists.
        :param source: source node
        :param target: target node
        :return:    True - if the edge exists
                    False - otherwise
        """

        if source in self.__din[target] and target in self.__dout[source]:
            return True
        return False

    def addEdge(self, source, target, cost):
        """
        Add edge form source node to target node to the graph.
        :param source: source node
        :param target: target node
        :param cost: cost of the edge
        :return:    True if the edge was added
                    False, otherwise
        """
        if self.isEdge(source, target):
            return False

        self.__din[target].append(source)
        self.__dout[source].append(target)
        self.__dcost.update({(source, target): cost})

        return True

    def removeEdge(self, source, target):
        """
        Remove an edge form source node to target node.
        :param source: source node
        :param target: target node
        :return:    True if the edge was removed
                    False if the edge did not exist
        """

        if not self.isEdge(source, target):
            return False

        self.__din[target].remove(source)
        self.__dout[source].remove(target)

        for edge in list(self.__dcost.keys()):
            if source in edge and target in edge:
                self.__dcost.pop(edge)

        return True

    def getCost(self, source, target):
        """
        Get the cost of an edge.
        :param source: source node
        :param target: target node
        :return: cost of the edge
        """

        return self.__dcost[(source, target)]

    def setCost(self, source, target, newCost):
        """
        Change the cost of the edge provided by the source and target nodes.
        :param source: source node
        :param target: target node
        :param newCost: new cost of the edge
        """
        self.__dcost[(source, target)] = newCost

    def readFromFile(self, filename):

        file = open(filename, "r")

        line = file.readline().strip().split()

        verticesNo = int(line[0])

        for vertex in range(0, verticesNo):
            self.addVertex(vertex)

        edgesNo = int(line[1])

        while edgesNo > 0:
            line = file.readline().strip().split()
            self.addEdge(int(line[0]), int(line[1]), int(line[2]))
            edgesNo -= 1

        file.close()

    def getOutboundOf(self, vertex):
        return deepcopy(self.__dout[vertex])

    def getInboundOf(self, vertex):
        return deepcopy(self.__din[vertex])

    def getEdges(self):
        return list(self.__dcost.keys())

    def getVertices(self):
        return list(self.__din.keys())

    def getCopy(self):
        return deepcopy(self)


def printMenu():

    menuStr = "\nMenu:\n" \
              "add-vertex <int> - Adds a vertex\n" \
              "remove-vertex <int> - Remove a vertex\n" \
              "in-degree <int> - Get the in degree of a vertex\n" \
              "out-degree <int> - Get the out degree of a vertex\n" \
              "outbound <int> - Get the outbound vertices of a vertex\n" \
              "inbound <int> - Get the inbound vertices of a vertex\n" \
              "vertices-num <int> - Get the number of vertices.\n" \
              "is-vertex <int> - Check if a vertex exists\n" \
              "add-edge <source> <target> <cost> - Adds an edge\n" \
              "remove-edge <source> <target> - Remove an edge\n" \
              "is-edge <source> <target> - Check if an edge exists\n" \
              "cost <source> <target> - Check edge cost\n" \
              "set-cost <source> <target> <new-cost> - Set cost of edge\n" \
              "vertices - Get all vertices with their outbounds\n"

    print(menuStr)

def menu():

    g = DCGraph()
    g.readFromFile("graph100k.txt")
    printMenu()
    while True:
        try:

            cmd = input(">>").strip().split()

            if cmd[0] == "add-vertex":
                if not g.addVertex(int(cmd[1])):
                    print("Vertex already exists.")

            elif cmd[0] == "remove-vertex":
                if not g.removeVertex(int(cmd[1])):
                    print("Vertex does not exist.")

            elif cmd[0] == "add-edge":
                if not g.addEdge(int(cmd[1]), int(cmd[2]), int(cmd[3])):
                    print("Edge already exists.")

            elif cmd[0] == "remove-edge":
                if not g.removeEdge(int(cmd[1]), int(cmd[2])):
                    print("Edge does not exist.")

            elif cmd[0] == "vertices":
                print(g.getVertices())

            elif cmd[0] == "vertices-num":
                print(g.getVertexNo())

            elif cmd[0] == "is-vertex":
                print(g.isVertex(int(cmd[1])))

            elif cmd[0] == "is-edge":
                print(g.isEdge(int(cmd[1]), int(cmd[2])))

            elif cmd[0] == "outbound":
                print(cmd[1] + " -> ", end="")
                for v in g.getOutboundOf(int(cmd[1])):
                    print(v, end=" ")
                print()

            elif cmd[0] == "inbound":
                print(cmd[1] + " <- ", end="")
                for v in g.getInboundOf(int(cmd[1])):
                    print(v, end=" ")
                print()

            elif cmd[0] == "out-degree":
                print(g.getOutDeg(int(cmd[1])))

            elif cmd[0] == "in-degree":
                print(g.getInDeg(int(cmd[1])))

            elif cmd[0] == "cost":
                print("Cost of edge " + str(cmd[1]) + " -> " + str(cmd[2]) + " :" + str(g.getCost(int(cmd[1]), int(cmd[2]))))

            elif cmd[0] == "set-cost":
                g.setCost(int(cmd[1]), int(cmd[2]), int(cmd[3]))

            elif cmd[0] == "help":
                printMenu()

            elif cmd[0] == "exit":
                return

            else:
                print("Invalid command!")
        except:
            print("Invalid input!")

menu()