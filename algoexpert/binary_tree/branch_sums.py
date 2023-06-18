# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    array = []
    helper(root, 0, array)
    return array


def helper(node, cur_sum, array):
    if node is None:
        return
    cur_sum += node.value
    if not node.left and not node.right:
        array.append(cur_sum)
        return
    helper(node.left, cur_sum, array)
    helper(node.right, cur_sum, array)
