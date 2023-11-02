from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time | O(h) space, h --> height of the tree
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if node is None:
                return 0, True
            left, left_balanced = dfs(node.left)
            right, right_balanced = dfs(node.right)
            return (
                1 + max(left, right),
                left_balanced and right_balanced and abs(left - right) <= 1
            )

        _, balanced = dfs(root)
        return balanced
