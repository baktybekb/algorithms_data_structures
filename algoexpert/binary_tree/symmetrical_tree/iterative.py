# https://www.algoexpert.io/questions/symmetrical-tree

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def symmetricalTree(tree):
    stack = [(tree.left, tree.right)]
    while stack:
        node1, node2 = stack.pop()
        if node1 == node2 is None:
            continue
        if not node1 or not node2 or node1.value != node2.value:
            return False
        stack.append((node1.left, node2.right))
        stack.append((node1.right, node2.left))
    return True
