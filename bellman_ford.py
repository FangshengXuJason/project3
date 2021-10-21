def bellman_ford(graph, source):
    # Step 1: Prepare the distance and predecessor for each node
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[source] = 0

    # Step 2: Relax the edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                # If the distance between the node and the neighbour is lower than the current, store it
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour], node

    # Step 3: Check for negative weight cycles
    for node in graph:
        for neighbour in graph[node]:
            if distance[neighbour] > distance[node] + graph[node][neighbour]:
                print("Negative Weight Cycle Found: Start Backtracking")
                actions = []
                child = node  # hard coded
                while child in predecessor.keys():
                    print("{1}\t-->\t\t{0}".format(predecessor[child], child))
                    actions.append(child)
                    child = predecessor[child]

                    if child is node:  # hard coded
                        actions.append(child)
                        actions.reverse()
                        print("actions: ", actions)
                        break
        break
    return distance, predecessor


if __name__ == '__main__':
    graph = {
        'a': {'b': -1, 'c': 4},
        'b': {'c': 3, 'd': 2, 'e': 2},
        'c': {},
        'd': {'b': 1, 'c': 5},
        'e': {'d': -3}
    }

    distance, predecessor = bellman_ford(graph, source='a')
    print(distance)

    graph = {
        'a': {'c': 3},
        'b': {'a': 2},
        'c': {'b': 7, 'd': 1},
        'd': {'a': 6},
    }

    distance, predecessor = bellman_ford(graph, source='a')
    print(distance)

    graph = {
        'a': {'b': 1, 'd':1},
        'b': {'c': 2},
        'c': {'a': -4},
        'd': {'a': 6, 'c': 1},
    }

    distance, predecessor = bellman_ford(graph, source='a')
    print(distance)