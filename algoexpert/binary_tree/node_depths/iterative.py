def nodeDepths(root, depth=0):
    stack = []
    total_depth = 0
    stack.append((root, 0))
    while stack:
        node, depth = stack.pop()
        if node is None:
            continue
        total_depth += depth
        stack.append((node.left, depth + 1))
        stack.append((node.right, depth + 1))
    return total_depth


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
