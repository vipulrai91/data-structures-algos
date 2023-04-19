# This is multiple problem program
# 1. Convert Edges to Graph
# 2. Traverse to find the edges
# 3. Make sure to add visited flag to avoid cyclic graph and infinte loop


from collections import defaultdict

undirected_edges = [["i", "j"], ["k", "i"], ["m", "k"], ["k", "l"], ["o", "n"]]


def helper_build_Graph(edges: list[list]) -> dict:
    """Helper function to return egdes as graph , creates adjacency list(dict in this case)

    Args:
        edges (list[list]): undirected edges 

    Returns:
        dict: graph
    """
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    return dict(graph)


def hasPath(graph, src, dest, visited):
    # base case
    if src == dest:
        return True
    # check visited to avoid acyclic graph
    if src in visited:
        return False
    visited.add(src)

    for neighbors in graph[src]:
        if hasPath(graph, neighbors, dest, visited) == True:
            return True

    return False


def undirectedPath(edges, nodeA, nodeB):
    graph = helper_build_Graph(edges)
    return hasPath(graph, nodeA, nodeB, set())


nodeA = "j"
nodeB = "m"
print(undirectedPath(undirected_edges, nodeA, nodeB))
