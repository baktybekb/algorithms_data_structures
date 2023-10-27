# https://www.algoexpert.io/questions/find-kth-largest-value-in-bst

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Info:
    def __init__(self, distance=0, last_value=None):
        self.distance = distance
        self.last_value = last_value


# O(h + k) time | O(h) space, h --> height of the tree
def findKthLargestValueInBst(tree, k):
    info = Info()

    def helper(node):
        if node is None or info.distance == k:
            return
        helper(node.right)
        if info.distance < k:
            info.distance += 1
            info.last_value = node.value
            helper(node.left)

    helper(tree)
    return info.last_value
