from collections import deque


# O(n) time | O(n) space
def nodeDepths(root):
    res = 0
    queue = deque([(root, 0)])
    while queue:
        node, depth = queue.popleft()
        res += depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return res


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
