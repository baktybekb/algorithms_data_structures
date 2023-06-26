# O(nlog(n)) | O(n) space --> because always insert() on a root node
def minHeightBst(array):
    return helper(array, None, 0, len(array) - 1)


def helper(array, bst, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if bst is None:
        bst = BST(array[mid])
    else:
        bst.insert(array[mid])
    helper(array, bst, start, mid - 1)
    helper(array, bst, mid + 1, end)
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
