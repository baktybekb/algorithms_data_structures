# https://www.algoexpert.io/questions/validate-bst

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(h) space, h --> height of the tree
def validateBst(node, left=float('-inf'), right=float('inf')):
    if node is None:
        return True
    if not (left <= node.value < right):
        return False
    return validateBst(node.left, left, node.value) and validateBst(node.right, node.value, right)

