class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeInfo:
    def __init__(self, manager=None):
        self.manager = manager


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tree_info = TreeInfo()
        self.helper(root, p, q, tree_info)
        return tree_info.manager

    def helper(self, node, p, q, tree_info):
        if node is None:
            return 0
        left = self.helper(node.left, p, q, tree_info)
        right = self.helper(node.right, p, q, tree_info)
        count = left + right
        if tree_info.manager:
            return count
        if node == p or node == q:
            count += 1
        if count == 2:
            tree_info.manager = node
        return count
