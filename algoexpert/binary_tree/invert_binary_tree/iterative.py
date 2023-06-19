def invertBinaryTree(node):
    if node is None:
        return node
    queue = [node]
    while queue:
        node = queue.pop()
        if node is None:
            continue
        node.left, node.right = node.right, node.left
        queue.append(node.left)
        queue.append(node.right)
    return node


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
