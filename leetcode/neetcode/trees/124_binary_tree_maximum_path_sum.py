from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time | O(h) space, h --> height of the tree
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int | float:
        info = float('-inf')

        def helper(node):
            if node is None:
                return float('-inf')
            left_branch = helper(node.left)
            right_branch = helper(node.right)

            child_branch = max(left_branch, right_branch)
            current_branch = max(child_branch + node.val, node.val)
            current_root = max(left_branch + right_branch + node.val, node.val)

            nonlocal info
            info = max(info, current_branch, current_root)
            return current_branch

        helper(root)
        return info
