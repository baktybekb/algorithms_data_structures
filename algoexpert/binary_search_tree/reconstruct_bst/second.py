# https://www.algoexpert.io/questions/reconstruct-bst

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Info:
    def __init__(self, root_idx=0):
        self.root_idx = root_idx


# O(n) time | O(n) space
def reconstructBst(array):
    info = Info()

    def helper(lower, upper):
        if info.root_idx == len(array):
            return None
        if not (lower <= array[info.root_idx] < upper):
            return None
        node = BST(array[info.root_idx])
        info.root_idx += 1
        node.left = helper(lower, node.value)
        node.right = helper(node.value, upper)
        return node

    helper(float('-inf'), float('inf'))
    return None
