# O(log(n)) time | O(log(n)) space
def findClosestValueInBst(tree, target):
    return helper(tree, target, tree.value)


def helper(node, target, closest):
    if node is None:
        return closest
    if abs(target - node.value) < abs(target - closest):
        closest = node.value
    if target < node.value:
        return helper(node.left, target, closest)
    elif target > node.value:
        return helper(node.right, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
