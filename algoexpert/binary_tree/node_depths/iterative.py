# https://www.algoexpert.io/questions/node-depths
from collections import deque


# O(n) time | O(n) space
def nodeDepths(root):
    queue = deque([root])
    res = depth = 0
    while queue:
        count = len(queue)
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res += count * depth
        depth += 1
    return res


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
