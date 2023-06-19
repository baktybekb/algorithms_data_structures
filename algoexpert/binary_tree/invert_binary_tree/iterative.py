def invertBinaryTree(node):
    if node is None:
        return node
    stack = [node]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        node.left, node.right = node.right, node.left
        stack.append(node.left)
        stack.append(node.right)
    return node


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
