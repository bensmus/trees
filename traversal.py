from node import Node
from datatypes import Stack, Queue

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(6)

A.left = B
A.right = C
B.left = D
D.left = E
D.right = F


def pre_order(node):
    if node == None:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)


print("===recursive pre-order===")
pre_order(A)


def pre_order_iterative(root):
    stack = Stack()
    stack.push(root)

    # Stack does not accept pushes of None,
    # it ignores them.

    while not stack.empty():
        # stack.to_console()

        node = stack.pop()
        print(node)
        stack.push(node.right)
        stack.push(node.left)


print("===iterative pre-order===")
pre_order_iterative(A)


def breadth_first(root):
    queue = Queue()
    queue.push(root)

    while not queue.empty():
        node = queue.pop()
        print(node)

        # when you push to a queue, they come to the back, not to the front!
        queue.push(node.right)
        queue.push(node.left)


print("===iterative breadth-first===")
breadth_first(A)
