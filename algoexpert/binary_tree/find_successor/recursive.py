# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(h) time | O(h) space, h --> height of the tree
def findSuccessor(tree, node):
    if node.right:
        return traverse_down(node.right)
    return traverse_up(node, node.parent)


def traverse_up(prev, parent):
    if parent is None:
        return None
    if parent.left == prev:
        return parent
    return traverse_up(parent, parent.parent)


def traverse_down(node):
    if node.left is None:
        return node
    return traverse_down(node.left)
