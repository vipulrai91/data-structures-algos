graph = {
    "a": ["b", "c"],
    # "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}


def depthFirstPrint(graph, source):
    stack = [source]
    depth_first_traversal = (
        []
    )  # hold the elements in DFS order , alternatively this can be printed as well

    while len(stack) > 0:
        current = stack.pop()
        depth_first_traversal.append(current)  # all the items in stack in DFS order

        for neighbor in graph[current]:
            stack.append(neighbor)  # keep appending all the nodes in the order
    return depth_first_traversal


depth_first_traversal = depthFirstPrint(graph=graph, source="a")
print(depth_first_traversal)


def depthFirstRecursive(graph, source):
    print(source)
    for neighbor in graph[source]:
        depthFirstRecursive(graph, neighbor)


depthFirstRecursive(graph=graph, source="a")
