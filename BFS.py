from node import Node
from datatypes import Stack, Queue


def breadth_first(root):
    queue = Queue()
    queue.push("separator")
    queue.push(root)

    height = 0
    while not queue.empty():
        node = queue.pop()
        if isinstance(node, Node):
            print(node)
            if not node.leaf():
                queue.push("separator")

                # queue ignores pushes of None, these are potential None pushes
                queue.push(node.left)
                queue.push(node.right)

        if node == "separator":
            print(f"height {height}")
            height += 1


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

A.left = B
A.right = C
B.left = D
D.left = E
D.right = F

breadth_first(A)
