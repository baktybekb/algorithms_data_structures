# https://www.algoexpert.io/questions/split-binary-tree

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space, h -- height of the tree
def splitBinaryTree(tree):
    total = tree_sum(tree)
    if total % 2 != 0:
        return 0
    target = total / 2
    res = backtrack_sum(tree, target)
    return target if res == target else 0


def backtrack_sum(tree, target):
    if tree is None:
        return 0
    left = backtrack_sum(tree.left, target)
    right = backtrack_sum(tree.right, target)
    if left == target or right == target:
        return target
    return left + right + tree.value


def tree_sum(tree):
    if tree is None:
        return 0
    return tree.value + tree_sum(tree.left) + tree_sum(tree.right)



