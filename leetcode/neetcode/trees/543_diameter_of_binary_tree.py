from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time | O(d) space, d --> depth of the tree
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node is None:
                return 0, 0
            left_path, left_root = helper(node.left)
            right_path, right_root = helper(node.right)
            return (
                max(left_path, right_path) + 1,
                max(left_path + right_path + 1, left_root, right_root)
            )

        _, root_path = helper(root)
        return root_path - 1
