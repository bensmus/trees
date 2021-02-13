class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return self.value.__str__()

    def leaf(self):
        return (self.left == None and self.right == None)
