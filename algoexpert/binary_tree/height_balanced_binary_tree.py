# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(node):
    is_balanced, h = helper(node)
    return is_balanced


def helper(node):
    if node is None:
        return True, 0
    left_balanced, left_height = helper(node.left)
    right_balanced, right_height = helper(node.right)
    height = 1 + max(left_height, right_height)
    if abs(left_height - right_height) > 1:
        return False, height
    return left_balanced and right_balanced, height
