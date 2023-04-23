largest_component = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}


def explore(graph, current, visited):
    if current in visited:
        return 0
    visited.add(current)
    size = 1
    if graph.get(current) != None:
        for neighbor in graph[current]:
            size += explore(graph, neighbor, visited)
    return size


def largest_Components(graph):
    longest_count = 0
    visited = set()

    for nodes in graph:
        explore_count = explore(graph, nodes, visited)
        if explore_count > longest_count:
            longest_count = explore_count

    return longest_count


print(largest_Components(largest_component))

