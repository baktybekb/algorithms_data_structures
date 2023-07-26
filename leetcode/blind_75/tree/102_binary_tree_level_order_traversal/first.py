"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time | O(n) space
class Solution:
    def levelOrder(self, root: TreeNode | None, depth=0) -> List[List[int]]:
        queue = [(root, depth)]
        result = []
        prev_depth = depth
        while queue:
            node, cur_depth = queue.pop(0)  # in theory O(1) time
            if node is None:
                continue
            if not result or prev_depth != cur_depth:
                result.append([node.val])
            else:
                result[-1].append(node.val)
            queue.append((node.left, cur_depth + 1))
            queue.append((node.right, cur_depth + 1))
            prev_depth = cur_depth
        return result
