# https://www.algoexpert.io/questions/invert-binary-tree

# O(n) time | O(h) space, h --> height of the tree
def invertBinaryTree(tree):
    if tree is None:
        return
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
