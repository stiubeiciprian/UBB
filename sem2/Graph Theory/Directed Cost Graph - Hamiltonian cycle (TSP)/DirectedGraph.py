import itertools
from copy import deepcopy

"""
6. Given a digraph with costs, find a minimum cost Hamiltonian cycle (i.e., solve the TSP)
"""

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

    def getAllSubsets(self, inputList):
        setFinalList = [()]
        for i in range(len(inputList)):
            setFinalList.extend(tuple(itertools.combinations(inputList, i + 1)))
        return setFinalList

    def travellingSalesmanProblem(self,startVertex):
        dist = {} # distance dict
        vertexList = self.getVertices()
        vertexList.remove(startVertex)
        parent = {}
        allSubsets = self.getAllSubsets(vertexList) # complexity 2^n
        vertexList.append(startVertex)
        for currentSet in allSubsets:
            for vertex in vertexList: # Computing distance to all vertices using the given set
                if len(currentSet) == 0: #empty set so we set the distance to startVertex - vertex edge
                    if self.isEdge(startVertex,vertex):
                        dist[(vertex,())] = self.getCost(startVertex,vertex)
                        parent[(vertex, currentSet)] = startVertex
                if vertex not in currentSet:
                    for element in currentSet:
                        index = currentSet.index(element)
                        preceedingSet = currentSet[:index] + currentSet[index+1:] # remove element form set
                        if self.isEdge(element,vertex): #updating distance
                            if (vertex,currentSet) not in dist or dist[element,preceedingSet] + self.getCost(element,vertex) < dist[(vertex,currentSet)]:
                                dist[(vertex,currentSet)] = dist[(element,preceedingSet)] + self.getCost(element,vertex)
                                parent[(vertex,currentSet)] = element


        path = [startVertex]
        preceedingSet = currentSet
        vertex = parent[(startVertex,preceedingSet)]
        while vertex !=startVertex: #path building
            path.append(vertex)
            index = preceedingSet.index(vertex)
            preceedingSet = preceedingSet[:index] + preceedingSet[index+1:]
            vertex = parent[(vertex, preceedingSet)]

        path.append(startVertex)
        path.reverse()

        return (dist[(startVertex,currentSet)],path)


g = DCGraph()
g.readFromFile("digraph-ex1.txt")
print(g.travellingSalesmanProblem(0)
