# https://www.algoexpert.io/questions/min-height-bst

# O(nlog(n)) time | O(n) space
def minHeightBst(array):
    return helper(array, 0, len(array) - 1)


def helper(array, start, end, bst=None):
    if start > end:
        return None
    mid = (start + end) // 2
    if bst:
        bst.insert(array[mid])
    else:
        bst = BST(array[mid])
    helper(array, start, mid - 1, bst)
    helper(array, mid + 1, end, bst)
    return bst


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
