# https://www.algoexpert.io/questions/binary-tree-diameter

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space, h --> height of the tree
def binaryTreeDiameter(tree):
    total = 0

    def helper(node):
        if node is None:
            return 0
        left = helper(node.left)
        right = helper(node.right)

        nonlocal total
        total = max(total, left + right)
        return 1 + max(left, right)

    helper(tree)
    return total
