tree = {
    "target": 12,
    "tree": {
        "nodes": [
            {"id": "10", "left": "5", "right": "15", "value": 10},
            {"id": "15", "left": "13", "right": "22", "value": 15},
            {"id": "22", "left": None, "right": None, "value": 22},
            {"id": "13", "left": None, "right": "14", "value": 13},
            {"id": "14", "left": None, "right": None, "value": 14},
            {"id": "5", "left": "2", "right": "5-2", "value": 5},
            {"id": "5-2", "left": None, "right": None, "value": 5},
            {"id": "2", "left": "1", "right": None, "value": 2},
            {"id": "1", "left": None, "right": None, "value": 1},
        ],
        "root": "10",
    },
}


# This is the class of the input tree. Do not edit.
class BST:
    """Define a class for BST it holds value and pointer to left and right 
    """

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBstHelper(tree, target, closest):
    if tree == None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest


def findClosestValueInBst(tree: BST, target: int):
    return findClosestValueInBstHelper(tree, target, int("inf"))
