# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(h) space, h --> height - max stack length
def repairBst(tree):
    prev = node1 = node2 = None
    current_node = tree
    stack = []
    while current_node or stack:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        if prev and prev.value > current_node.value:
            if node1 is None:
                node1 = prev
            node2 = current_node
        prev = current_node
        current_node = current_node.right
    node1.value, node2.value = node2.value, node1.value
    return tree
