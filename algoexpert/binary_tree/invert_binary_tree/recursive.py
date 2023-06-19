def invertBinaryTree(node):
    if node is None:
        return
    node.left, node.right = node.right, node.left
    invertBinaryTree(node.left)
    invertBinaryTree(node.right)
    return node


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
