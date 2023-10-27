# https://www.algoexpert.io/questions/min-height-bst

# O(n) time | O(n) space
def minHeightBst(array):
    return helper(0, len(array) - 1, array)


def helper(start, end, array):
    if start > end:
        return None
    mid = (start + end) // 2
    node = BST(array[mid])
    node.left = helper(start, mid - 1, array)
    node.right = helper(mid + 1, end, array)
    return node


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
