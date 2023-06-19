# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(n) time | O(1) space
def findSuccessor(tree, node):
    if node.right:
        return find_left_node(node.right)
    parent = node.parent
    if parent is None:
        return None
    if parent.right == node:
        return parent.parent
    return parent  # parent.left == node


def find_left_node(node):
    while node and node.left:
        node = node.left
    return node
