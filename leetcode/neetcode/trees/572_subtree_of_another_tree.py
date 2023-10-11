from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n * m) time | O(h) space, h --> height of root tree
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same_tree(self, p, q):
        if not p or not q:
            return p == q
        if p.val != q.val:
            return False
        return self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)
