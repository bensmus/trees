from collections import deque


class Stack:
    def __init__(self, *args):
        self.data = deque(args)

    def push(self, value):
        if value == None:
            return
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def empty(self):
        return (len(self.data) == 0)

    def to_console(self):
        print("---stack top---")
        for elem in self.data:
            print(elem)
        print("---------------\n")


# overwrite some methods of stack
class Queue(Stack):
    def push(self, value):
        if value == None:
            return
        # appendleft instead of append
        self.data.appendleft(value)

    def to_console(self):
        print("---queue head---")
        for elem in self.data:
            print(elem)
        print("---queue tail----\n")


if __name__ == "__main__":
    from node import Node

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

    stack = Stack()
    stack.push(A)
    stack.to_console()

    stack.pop()
    stack.push(A.left)
    stack.push(A.right)
    stack.to_console()

    stack.push(F.left)
    stack.to_console()

    print("============")

    # queue time!!
    queue = Queue()

    queue.push(A)
    queue.to_console()

    queue.pop()
    queue.push(A.left)
    queue.push(A.right)
    queue.to_console()

    queue.push(F.left)
    queue.to_console()
