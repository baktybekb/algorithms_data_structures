from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time | O(h) space, h --> height of the tree
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left = max(left, 0)
            right = max(right, 0)

            node_sum = max(left + right + node.val, node.val)
            res[0] = max(res[0], node_sum)
            return node.val + max(left, right)

        dfs(root)
        return res[0]
