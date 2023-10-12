from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, visited=0, last_val=None):
        self.visited = visited
        self.last_val = last_val


# (h + k) time | O(h) space, h --> height of the tree
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        info = TreeInfo()

        def helper(node):
            if node is None or info.visited == k:
                return
            helper(node.left)
            if info.visited < k:
                info.visited += 1
                info.last_val = node.val
                helper(node.right)

        helper(root)
        return info.last_val










