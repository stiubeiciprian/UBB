import heapq

class Graph:
    def __init__(self, fileName):
        self.In = {}
        self.Out = {}
        self.Cost = {}
        self.Vertices = self.readVertices(fileName)
        for i in range(0, self.Vertices):
            self.In[i] = []
            self.Out[i] = []
        self.readFromFile(fileName)

    def getCosts(self):
        return self.Cost

    @staticmethod
    def readVertices(fileName):
        f = open(fileName, "r")
        lines = f.read().strip("\n")
        line = lines.split(" ")
        return int(line[0])

    def readFromFile(self, fileName):
        f = open(fileName, "r")
        lines = f.readline().strip()
        lines = f.readline().strip()
        while lines != "":
            line = lines.split(" ")
            x = int(line[0])
            y = int(line[1])
            c = int(line[2])
            self.addEdge(x, y, c)
            lines = f.readline().strip()

    def getNumber(self):
        return len(self.In.keys())

    def parse(self):
        return list(self.In.keys())

    def parseIn(self, x):
        if self.isVertex(x):
            return self.In[x]
        return False

    def parseOut(self, x):
        if self.isVertex(x):
            return self.Out[x]
        return False

    def addEdge(self, x, y, c):
        # x -> y, with the cost c
        if not self.isEdge(x, y):
            self.In[y].append(x)
            self.Out[x].append(y)
            self.Cost[(x, y)] = c
            return True
        return False

    def isEdge(self, x, y):
        # looks for edge x->y
        for i in self.Out[x]:
            if i == y:
                return True
        return False

    def removeEdge(self, x, y):
        if self.isEdge(x, y):
            self.In[y].remove(x)
            self.Out[x].remove(y)
            del self.Cost[(x, y)]
            return True
        return False

    def addVertex(self, x):
        if not self.isVertex(x):
            self.In[x] = []
            self.Out[x] = []
            return True
        return False

    def isVertex(self, x):
        if x in self.parse():
            return True
        return False

    def removeVertex(self, x):
        if self.isVertex(x):
            for i in self.parseIn(x):
                self.removeEdge(i, x)
            for i in self.parseOut(x):
                self.removeEdge(x, i)
            del self.In[x]
            del self.Out[x]
            return True
        return False

    def getCost(self, x, y):
        if self.isEdge(x, y):
            return self.Cost[(x, y)]
        return False

    def setCost(self, x, y, new_cost):
        if self.isEdge(x, y):
            self.Cost[(x, y)] = new_cost
            return True
        return False

    def printGraph(self):
        for i in self.parse():
            if len(self.In[i]) == len(self.Out[i]) == 0:
                print(i, "is an isolated vertex")
            else:
                for j in self.Out[i]:
                    print(i, "->", j, "having the cost:", self.Cost[(i, j)])



def getPath(prev, final):
    """
        In:
            - prev = the dictionary of parent nodes for each node of a graph
            - final = the final node of a path

        Description:
            - returns a list of vertices representing the shortest path from final to start

        Output:
            - a list of nodes
    """
    path = []
    if final not in prev:
        return None # the path could not be found
    while final != None:
        path.append(final)
        final = prev[final]
    return path

def dijkstra(graph, start, final, costs):
    """
        In:
            - graph = the graph on which we find the shortest path
            - start = the starting node of the path
            - final = the end point of the path
            - costs = the cost dictionary, having as keys pairs of vertices representing edges x->y
        Out:
            - a tuple containing:
                - path = a list of vertices representing the mincost path
                - pCost = the cost of the path
            - None if there is no path between the given vertices
    """
    dist = {}
    prev = {}
    prev[final] = None
    q = []
    dist[final] = 0
    heapq.heappush(q, (dist[final], final))
    while len(q) > 0:
        dummy, x = heapq.heappop(q)
        if(dummy == dist[x]):
            for y in graph.parseIn(x):
                if y not in prev or dist[y] > dist[x] + costs[(y, x)]:
                    prev[y] = x
                    dist[y] = dist[x] + costs[(y, x)]
                    heapq.heappush(q, (dist[y], y))
    if getPath(prev, start) is None:
        return None
    return (getPath(prev, start), dist[start])



graph = Graph("graph1k.txt")

while(True):
    try:
        v1 = int(input("Start vertex:"))
        v2 = int(input("End vertex: "))
        res = dijkstra(graph, v1, v2, graph.getCosts())

        if res is None:
            print("No path found between the two vertices.")
        else:
            print("Path:", end="")

            for v in range(len(res[0])-1):
                print(str(res[0][v]) + " -> ", end="")

            print(res[0][len(res[0]) - 1])
            print("Cost:", end="")
            print(res[1])

        print("============================================================")
    except:
        print("Invalid input!")