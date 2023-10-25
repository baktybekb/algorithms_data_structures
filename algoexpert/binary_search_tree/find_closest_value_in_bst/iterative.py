# https://www.algoexpert.io/questions/find-closest-value-in-bst

# O(log(n)) time | O(1) space
def findClosestValueInBst(tree, target):
    closest = tree.value
    while tree:
        if abs(target - tree.value) < abs(target - closest):
            closest = tree.value
        if target < tree.value:
            tree = tree.left
        else:
            tree = tree.right
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
