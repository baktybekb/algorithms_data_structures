# https://www.algoexpert.io/questions/height-balanced-binary-tree

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space, h --> height of the tree
def heightBalancedBinaryTree(tree):

    def helper(node):
        if node is None:
            return True, 0
        left_balanced, left_height = helper(node.left)
        right_balanced, right_height = helper(node.right)
        if not left_balanced or not right_balanced:
            return False, 0
        return (
            abs(left_height - right_height) <= 1,
            1 + max(left_height, right_height)
        )

    balanced, _ = helper(tree)
    return balanced
