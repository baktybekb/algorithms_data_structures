# https://www.algoexpert.io/questions/symmetrical-tree

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space, h --> height of the tree
def symmetricalTree(tree):

    def helper(node1, node2):
        if node1 == node2 is None:
            return True
        elif not node1 or not node2 or node1.value != node2.value:
            return False
        return (
            helper(node1.left, node2.right) and
            helper(node1.right, node2.left)
        )

    return helper(tree.left, tree.right)
