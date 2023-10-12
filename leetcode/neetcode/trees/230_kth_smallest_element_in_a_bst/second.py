from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(h + k) time | O(h) space, h --> height of the tree
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        count = 0
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            node = node.right
