class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeInfo:
    def __init__(self, manager=None, count=0):
        self.manager = manager
        self.count = count


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root, p, q).manager

    def helper(self, node, p, q):
        count = 0
        for child in (node.left, node.right):
            if child is None:
                continue
            tree_info = self.helper(child, p, q)
            if tree_info.manager:
                return tree_info
            count += tree_info.count
        if node == p or node == q:
            count += 1
        return TreeInfo(manager=node if count == 2 else None, count=count)
