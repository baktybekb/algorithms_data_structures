# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(d) space, d == depth
def validateBst(tree):
    return helper(tree, float('-inf'), float('inf'))


def helper(node, smallest, greatest):
    if node is None:
        return True
    if not smallest <= node.value < greatest:
        return False
    left = helper(node.left, smallest, node.value)
    right = helper(node.right, node.value, greatest)
    return left and right

