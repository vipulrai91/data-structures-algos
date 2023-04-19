class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")


print(a.value)
print(b.value)
print(c.value)
print(d.value)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
