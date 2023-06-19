# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(n) time | O(n) space
def findSuccessor(tree, node):
    array = []
    helper(tree, array)
    for i in range(len(array) - 1):
        if array[i] == node:
            return array[i + 1]
    return None


def helper(node, array):
    if node is None:
        return
    helper(node.left, array)
    array.append(node)
    helper(node.right, array)



