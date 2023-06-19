# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(node):
    """d - diameter, h - height """
    d, h = helper(node)
    return d


def helper(node):
    if node is None:
        return 0, 0
    left_d, left_h = helper(node.left)
    right_d, right_h = helper(node.right)
    return max(left_d + right_d, left_h + right_h), max(left_h, right_h) + 1
