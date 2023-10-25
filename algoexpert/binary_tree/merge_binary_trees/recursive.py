# https://www.algoexpert.io/questions/merge-binary-trees

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n + m) time | O(h) space, h --> height of the tree1
def mergeBinaryTrees(tree1, tree2):
    if not tree1 or not tree2:
        return tree1 if tree1 else tree2
    tree1.value += tree2.value
    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = mergeBinaryTrees(tree1.right, tree2.right)
    return tree1

