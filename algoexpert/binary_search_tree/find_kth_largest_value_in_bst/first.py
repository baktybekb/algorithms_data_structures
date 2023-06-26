# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def findKthLargestValueInBst(tree, k):
    array = []
    in_order_traverse(tree, array)
    if array:
        return array[-k]
    return -1


def in_order_traverse(node, array):
    if node is None:
        return
    in_order_traverse(node.left, array)
    array.append(node.value)
    in_order_traverse(node.right, array)
