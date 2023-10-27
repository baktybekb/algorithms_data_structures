# https://www.algoexpert.io/questions/reconstruct-bst

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n ^ 2) time | O(n) space
def reconstructBst(array):
    if not array:
        return None
    root_value = array[0]
    right_idx = len(array)
    for i in range(1, len(array)):
        if array[i] >= root_value:
            right_idx = i
            break
    left = reconstructBst(array[1:right_idx])
    right = reconstructBst(array[right_idx:])
    return BST(root_value, left, right)

