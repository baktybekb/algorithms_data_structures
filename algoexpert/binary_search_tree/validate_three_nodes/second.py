# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(d) time | O(1) space, d --> distance between nodeOne and nodeThree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    search1 = nodeOne
    search2 = nodeThree
    found = False
    while True:
        if search1 == search2 or search1 == search2 is None:
            break
        if search1 == nodeTwo or search2 == nodeTwo:
            found = True
            break
        if search1:
            search1 = search1.left if nodeTwo.value < search1.value else search1.right
        if search2:
            search2 = search2.left if nodeTwo.value < search2.value else search2.right
    if not found:
        return False
    current = nodeTwo
    descendent = nodeThree if search1 == nodeTwo else nodeOne
    while current and current != descendent:
        current = current.left if descendent.value < current.value else current.right
    return True if current else False

