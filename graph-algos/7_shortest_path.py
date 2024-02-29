# Depth first would be faster, using queues
from collections import defaultdict

edges = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]


def convert_edges_to_adjacency_list(edges):
    graph = defaultdict(list)

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    return dict(graph)


graph = convert_edges_to_adjacency_list(edges)


def findShortestPath(graph, src, dest):
    path_length = 0
    visited = set()
    # base case
    if src == dest:
        return path_length
    for node in graph:
        print(node)


print(findShortestPath(graph=graph, src="w", dest="z"))
