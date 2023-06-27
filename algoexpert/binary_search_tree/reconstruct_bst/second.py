# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, root_idx):
        self.root_idx = root_idx


# O(n) time | O(h) space, h --> height of the tree
def reconstructBst(preOrderTraversalValues):
    tree_info = TreeInfo(0)
    return helper(preOrderTraversalValues, float('-inf'), float('inf'), tree_info)


def helper(array, lower, upper, tree_info):
    if tree_info.root_idx == len(array) or not lower <= array[tree_info.root_idx] < upper:
        return None
    root_idx = tree_info.root_idx
    bst = BST(array[root_idx])
    tree_info.root_idx += 1
    bst.left = helper(array, lower, array[root_idx], tree_info)
    bst.right = helper(array, array[root_idx], upper, tree_info)
    return bst

