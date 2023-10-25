# https://www.algoexpert.io/questions/find-closest-value-in-bst

# O(log(n)) time | O(h) space, h --> height of the tree
def findClosestValueInBst(tree, target):
    return helper(tree, target, tree.value)

def helper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - tree.value) < abs(target - closest):
        closest = tree.value
    if target < tree.value:
        return helper(tree.left, target, closest)
    else:
        return helper(tree.right, target, closest)


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
