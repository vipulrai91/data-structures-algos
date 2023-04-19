adjacency_dict = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": [],
    "e": ["b"],
    "f": ["d"],
}


# Depth fist traversal on graph  - go deeper on the selected path ,
# stop at dead end , move to other neighbor of root(starting) node in this case
# - Exploring one direction to the end before switching since there are no other possibilites

# Breadth first traversal on graph - move to all the adjacent nodes (neighbor , starting from any)
#  , before moving to next nodes
# Tend to explore all direction evenly instead of favoring some direction/node

# Depth first uses - stack
# Breadth first uses - queue
