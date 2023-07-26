# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time | O(n) space
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        result = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node is None:
                    continue
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if level:
                result.append(level)
        return result
