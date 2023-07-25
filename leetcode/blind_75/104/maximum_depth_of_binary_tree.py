# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time complexity | O(d), d - depth of the tree
    def maxDepth(self, root: TreeNode = None, depth=0) -> int:
        if root is None:
            return depth
        return max(
            self.maxDepth(root.left, depth + 1),
            self.maxDepth(root.right, depth + 1)
        )
