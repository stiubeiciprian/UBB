from copy import deepcopy


class Graph:

    def __init__(self, verticesNo = 0):
        self.__edges = {}

        for i in range(verticesNo):
            self.addVertex(i)

    def addVertex(self, vertex):
        """
        Add a vertex to the graph.
        :param vertex: vertex (int)
        :return:    True - if the vertex was added
                    False - if the vertex already existed
        """

        if self.isVertex(vertex):
            return False

        self.__edges.update({vertex: []})

        return True

    def removeVertex(self, vertex):
        """
        Remove a vertex from the graph.
        :param vertex: vertex (int)
        :return:    True - if the vertex was removed
                    False - if the vertex did not exist
        """

        if not self.isVertex(vertex):
            return False

        for v in self.__edges[vertex]:
            self.__edges[v].remove(vertex)

        self.__edges.pop(vertex)

        return True

    def isVertex(self, vertex):
        """
        Check if vertex exists.
        :param vertex: Vertex
        :return:    True - if the vertex exists
                    False - otherwise
        """

        return vertex in self.__edges.keys()


    def getVertexNo(self):
        """
        Gets the number of vertices.
        :return: number of vertices
        """

        return len(self.__edges)

    def isEdge(self, source, target):
        """
        Check if the edge exists.
        :param source: source node
        :param target: target node
        :return:    True - if the edge exists
                    False - otherwise
        """

        if source in self.__edges[target]:
            return True
        return False

    def addEdge(self, source, target):
        """
        Add edge form source node to target node to the graph.
        :param source: source node
        :param target: target node
        :return:    True if the edge was added
                    False, otherwise
        """
        if self.isEdge(source, target):
            return False

        self.__edges[target].append(source)
        self.__edges[source].append(target)

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

        self.__edges[target].remove(source)
        self.__edges[source].remove(target)

        return True

    def readFromFile(self, filename):

        file = open(filename, "r")

        line = file.readline().strip().split()

        verticesNo = int(line[0])

        for vertex in range(0, verticesNo):
            self.addVertex(vertex)

        edgesNo = int(line[1])

        while edgesNo > 0:
            line = file.readline().strip().split()
            self.addEdge(int(line[0]), int(line[1]))
            edgesNo -= 1

        file.close()

    def getVertices(self):
        return list(self.__edges.keys())

    def getCopy(self):
        return deepcopy(self)

    def BFS(self, source, visited):

        component = []
        queue = []

        queue.append(source)
        visited[source] = True

        while queue:

            source = queue.pop(0)
            component.append(source)

            for i in self.__edges[source]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True

        return component

    def connectedComponents(self):
        visited = [False] * self.getVertexNo()

        i = 0
        for vertex in range(self.getVertexNo()):
            if visited[vertex] is False:
                i += 1
                print("Component " + str(i) + ":", end="")
                print(self.BFS(vertex, visited))
    def getOutbound(self, vertex):
        return self.__edges[vertex]

def printMenu():

    menuStr = "\nMenu:\n" \
              "add-vertex <int> - Adds a vertex\n" \
              "remove-vertex <int> - Remove a vertex\n" \
              "vertices-num <int> - Get the number of vertices.\n" \
              "is-vertex <int> - Check if a vertex exists\n" \
              "add-edge <source> <target> <cost> - Adds an edge\n" \
              "remove-edge <source> <target> - Remove an edge\n" \
              "is-edge <source> <target> - Check if an edge exists\n" \
              "compall - Get all connected components\n"

    print(menuStr)

def menu():

    g = Graph()
    g.readFromFile("graph.txt")
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
                if not g.addEdge(int(cmd[1]), int(cmd[2])):
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

            elif cmd[0] == "help":
                printMenu()

            elif cmd[0] == "compall":
                g.connectedComponents()

            elif cmd[0] == "comp":
                visited = [False] * g.getVertexNo()
                connected_nodes = g.BFS(int(cmd[1]),visited)
                print("Connected nodes:")
                for v in connected_nodes:
                    print(v,end=", ")


                set_of_edges = []
                print("\nEdges:")
                for v in connected_nodes:
                    for connected_vertex in g.getOutbound(v):
                        if connected_vertex in connected_nodes:
                            pair = [v,connected_vertex]
                            if pair not in set_of_edges:
                                set_of_edges.append(pair)

                for edge in set_of_edges:
                    print(edge)

            elif cmd[0] == "exit":
                return

            else:
                print("Invalid command!")
        except:
            print("Invalid input!")

menu()