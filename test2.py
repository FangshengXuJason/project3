# Python3 program for Bellman-Ford's single source
# shortest path algorithm.

# Class to represent a graph


class Graph2:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []
        self.parent = {}

    # function to add an edge to graph
    def addEdge(self, u, v, w):

        self.graph.append([u, v, w])

    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        i = 0
        for item in dist:
            print("{0}\t\t{1}".format(i, item))
            i = i + 1

    def printParent(self,):
        print("Print Parent")
        for child in self.parent.keys():
            print("{0}\t-->\t\t{1}".format(child, self.parent[child]))

    def returnPath(self, end):
        actions = []
        v = end
        while v in self.parent.keys():
            actions.append(v)
            v = self.parent[v]
            if v is end:
                actions.append(v)
                actions.reverse()
                return actions
        return actions
    # src: start node/ edge
    def BellmanFord(self, src):

        distance = [float("Inf")] * self.V
        distance[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    self.parent[v] = u
        self.printArr(distance)
        self.printParent()

        for u, v, w in self.graph:
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                print("Graph contains negative weight cycle")
                print(self.returnPath(u))
                return




# g = Graph2(5)

# g.addEdge(0, 1, -1)
# g.addEdge(2, 0, -3)
# g.addEdge(1, 2, 3)
#
# g.addEdge(2, 0, -3) # added
#
# g.addEdge(1, 3, 2)
# g.addEdge(1, 4, 2)
# g.addEdge(3, 2, 5)
# g.addEdge(3, 1, 1)
# g.addEdge(4, 3, -3)

g = Graph2(4)

g.addEdge(0,1,1)
# g.addEdge(1,0,-1)

g.addEdge(1,2,2)
# g.addEdge(2,1,-2)

g.addEdge(2,0,-4)
# g.addEdge(0,2,4)

g.addEdge(0,3,1)
# g.addEdge(3,0,-1)

g.addEdge(3,2,-1)
# g.addEdge(2,3,1)

# Print the solution
g.BellmanFord(0)

