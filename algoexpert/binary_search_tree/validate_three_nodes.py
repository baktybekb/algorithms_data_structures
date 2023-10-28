# https://www.algoexpert.io/questions/validate-three-nodes

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(d) time | O(1) space, d --> distance between node_one and node_three
# O(h) time | O(1) space, h --> height of the tree, worst case when node_one == node_one == None
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    first, second = nodeOne, nodeThree

    while True:
        if (first is None and second is None) or (first == nodeThree or second == nodeOne):
            return False
        if first == nodeTwo or second == nodeTwo:
            break
        if first:
            first = first.left if nodeTwo.value < first.value else first.right
        if second:
            second = second.left if nodeTwo.value < second.value else second.right

    ancestor = first if first == nodeTwo else second
    descendant = nodeThree if first == nodeTwo else nodeOne

    while ancestor and ancestor != descendant:
        ancestor = ancestor.left if descendant.value < ancestor.value else ancestor.right
    return ancestor is not None
