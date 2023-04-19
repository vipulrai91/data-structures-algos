# Acyclic -> there is not infiite path and the traversal never reaches the root node

# graph = {
#     "f": ["g", "i"],
#     "g": ["h"],
#     "i": ["g", "k"],
#     "j": ["i"],
#     "k": []
#     }

graph = {"f": ["g", "i"], "g": ["h"], "i": ["g", "k"], "j": ["i"], "k": [], "h": []}
source_node = "j"
destination_node = "k"


def has_path(graph, source_node, destination_node):
    stack = [source_node]
    while len(stack) > 0:
        current = stack.pop()

        for neighbors in graph[current]:
            if neighbors == destination_node:
                print(neighbors)
                return True
            else:
                stack.append(neighbors)

    return False


print(has_path(graph=graph, source_node=source_node, destination_node=destination_node))


def has_path_recursion_dfs(graph, src, dest):
    # DFS Solution
    # base case
    if src == dest:
        return True
    for neighbors in graph[src]:
        if has_path_recursion_dfs(graph, neighbors, dest) == True:
            return True
    return False


print(has_path_recursion_dfs(graph, source_node, destination_node))


def has_path_recursion_bfs(graph, src, dest):
    # BFS Solution
    # base case
    queue = [src]

    while len(queue) > 0:
        current = queue.pop()
        if current == dest:
            return True
        for neighbors in graph[current]:
            queue.insert(0, neighbors)

    return False


print(has_path_recursion_bfs(graph, source_node, destination_node))
