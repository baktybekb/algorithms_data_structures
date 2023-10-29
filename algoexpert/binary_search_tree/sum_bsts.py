#  https://www.algoexpert.io/questions/sum-bsts
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space, h --> height of the tree
def sumBsts(tree):
    total = 0

    def helper(node):
        if node is None:
            return True, float('inf'), float('-inf'), 0, 0
        left_bst, left_min, left_max, left_size, left_sum = helper(node.left)
        right_bst, right_min, right_max, right_size, right_sum = helper(node.right)
        bst = left_bst and right_bst and left_max < node.value <= right_min
        size = 1 + left_size + right_size
        root_sum = node.value + left_sum + right_sum
        if bst and size >= 3:
            nonlocal total
            total += root_sum
            root_sum = 0
        return bst, min(left_min, node.value), max(right_max, node.value), size, root_sum

    helper(tree)
    return total
