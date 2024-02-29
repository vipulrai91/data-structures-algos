# Logic -


graph = {0: [8, 1, 5], 1: [0], 5: [0, 8], 2: [3, 4], 3: [2, 4], 4: [3, 2]}


def connectedCompontentsCount(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph, node, visited) == True:
            count += 1
    return count


def explore(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)
    if graph.get(current) != None:
        for neighbor in graph[current]:
            explore(graph, neighbor, visited)

    return True


print(connectedCompontentsCount(graph))
