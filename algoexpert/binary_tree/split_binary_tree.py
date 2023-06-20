# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(h) space
def splitBinaryTree(tree):
    desired_sum = total_size(tree) / 2
    _, can_be_split = try_subtree(tree, desired_sum)
    return desired_sum if can_be_split else 0


def total_size(node):
    if node is None:
        return 0
    return node.value + total_size(node.left) + total_size(node.right)


def try_subtree(node, desired_sum):
    if node is None:
        return 0, False
    left_sum, left_split = try_subtree(node.left, desired_sum)
    right_sum, right_split = try_subtree(node.right, desired_sum)
    current_sum = left_sum + right_sum + node.value
    current_split = left_split or right_split or current_sum == desired_sum
    return current_sum, current_split
