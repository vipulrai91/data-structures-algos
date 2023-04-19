graph = {
    # "a": ["b", "c"],
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}


def breadthFirstTraversalPrint(graph, source):
    queue = [source]

    while len(queue) > 0:
        current = queue.pop()
        print(current)
        for neighbor in graph[current]:
            queue.insert(0, neighbor)


breadthFirstTraversalPrint(graph, "a")
