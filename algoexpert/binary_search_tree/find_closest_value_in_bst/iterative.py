# O(log(n)) time | O(1) space
def findClosestValueInBst(tree, target):
    closest = tree.value
    node = tree
    while node:
        if abs(target - node.value) < abs(target - closest):
            closest = node.value
        if target < node.value:
            node = node.left
        else:
            node = node.right
    return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
