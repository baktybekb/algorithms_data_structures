# https://www.algoexpert.io/questions/branch-sums

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(n) space
def branchSums(root):
    res = []

    def helper(node, prev_sum):
        if node is None:
            return
        prev_sum += node.value
        if node.left is None and node.right is None:
            res.append(prev_sum)
            return
        helper(node.left, prev_sum)
        helper(node.right, prev_sum)

    helper(root, 0)
    return res
