# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n^2) time | O(n) space
def reconstructBst(array):
    if len(array) == 0:
        return
    right_idx = len(array)
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            right_idx = i
            break
    bst = BST(array[0])
    bst.left = reconstructBst(array[1:right_idx])
    bst.right = reconstructBst(array[right_idx:])
    return bst
