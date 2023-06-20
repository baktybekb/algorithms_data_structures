# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space - h - height
def symmetricalTree(tree):
    # Write your code here.
    return False


def helper(left, right):
    if not left and not right:
        return True
    if not left or not right or left.value != right.value:
        return False
    return helper(left.left, right.right) and helper(left.right, right.left)
