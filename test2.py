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
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def returnPath(self, end, start):
        actions = []
        v = end
        while (v in self.parent.keys()) and (v is not start):
            parent = self.parent[v]
            actions.append(v)
            v = self.parent[parent]
        actions.reverse()
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
        for u, v, w in self.graph:
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                print("Graph contains negative weight cycle")
                print(self.returnPath(v, src))
                return




g = Graph2(5)

g.addEdge(0, 1, -1)
g.addEdge(2, 0, -3)
g.addEdge(1, 2, 3)

g.addEdge(2, 0, -3) # added

g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
# Print the solution
g.BellmanFord(0)

# Initially, Contributed by Neelam Yadav
# Later On, Edited by Himanshu Garg
