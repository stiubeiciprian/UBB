import heapq
from copy import deepcopy

"""
3. Write a program that, given a graph with costs, does the following:

verify if the corresponding graph is a DAG and performs a topological sorting of 
the activities using the algorithm based on depth-first traversal (Tarjan's algorithm);
if it is a DAG, finds a highest cost path between two given vertices, in O(m+n).
"""


# noinspection PyPep8Naming
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




    def topoSortDFS(self, x, sorted, fullyProcessed, inProcess):
        inProcess.add(x)
        for y in self.getInboundOf(x):
            if y in inProcess:
                return False
            else:
                if y not in fullyProcessed:
                    ok = self.topoSortDFS(y, sorted, fullyProcessed, inProcess)
                    if not ok:
                        return False
        inProcess.remove(x)
        sorted.append(x)
        fullyProcessed.add(x)
        return True

    def topoSort(self):
        sorted = []
        fullyProcess = set()
        inProcess = set()
        for x in self.getVertices():
            if x not in fullyProcess:
                ok = self.topoSortDFS(x, sorted, fullyProcess, inProcess)
                if not ok:
                    sorted = []
                    return
        return sorted


    def getLongestDistanceInDAG(self, start, end):
        if self.isVertex(start) is not True or self.isVertex(end) is not True:
            raise ValueError("One of the vertices does not exist\n")
        sorted = self.topoSort()
        if sorted is None:
            return None
        parent = {}
        distances = dict.fromkeys(sorted, None)
        distances[start] = 0
        for vertex in sorted:
            for neighbor in self.getOutboundOf(vertex):
                if distances[vertex] is not None:
                    if distances[neighbor] is None or distances[neighbor] < distances[vertex] + self.getCost(vertex,neighbor):
                        parent[neighbor] = vertex
                        distances[neighbor] = distances[vertex] + self.getCost(vertex, neighbor)

        if distances[end] is None:
            return None
        path = []
        vertex = end
        while vertex != start:
            path.append(vertex)
            vertex = parent[vertex]
        path.append(start)
        path.reverse()
        return (distances[end], path)


g = DCGraph()
g.readFromFile("graph1k.txt")

result = g.topoSort()

if result is None:
    print("Not a DAG")
else:
    print("Topological order:")
    print(result)

    while(True):

        cmd = input(">>")

        if cmd == "exit":
            break
        try:
            x = input("Source:")
            y = input("Target:")
            print(g.getLongestDistanceInDAG(int(x),int(y)))
        except ValueError as v:
            print(v)
