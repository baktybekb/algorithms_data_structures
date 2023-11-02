class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time | O(h) space, h --> height of the tree
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nodes = [0]

        def helper(node, max_val):
            if node is None:
                return
            if node.val >= max_val:
                nodes[0] += 1
                max_val = node.val
            helper(node.left, max_val)
            helper(node.right, max_val)

        helper(root, root.val)
        return nodes[0]
