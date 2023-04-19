from collections import defaultdict

undirected_edges = [["i", "j"], ["k", "i"], ["m", "k"], ["k", "l"], ["o", "n"]]


def helper_buildGraph(edges: list[list]) -> dict:
    """Helper function to return egdes as graph

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


graph = helper_buildGraph(undirected_edges)
print(graph)
