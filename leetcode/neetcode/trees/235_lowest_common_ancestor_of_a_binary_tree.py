class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeInfo:
    def __init__(self, ancestor=None, value=0):
        self.ancestor = ancestor
        self.value = value


# O(log(n)) time | O(1) space
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        left = p.val if p.val <= q.val else q.val
        right = p.val if p.val > q.val else q.val
        while True:
            if root.val < left and root.val < right:
                root = root.right
            elif root.val > left and root.val > right:
                root = root.left
            elif left <= root.val <= right:
                break
        return root

