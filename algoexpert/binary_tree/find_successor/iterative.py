# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(h) time | O(1) space, h --> height of the tree
def findSuccessor(tree, node):
    if node.right:
        return traverse_down(node.right)
    parent = node.parent
    prev = node
    while parent:
        if parent.left == prev:
            return parent
        prev = parent
        parent = parent.parent
    return None


def traverse_down(node):
    while node and node.left:
        node = node.left
    return node
