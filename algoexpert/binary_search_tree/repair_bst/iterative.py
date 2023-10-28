# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Info:
    def __init__(self, one=None, two=None, prev=None):
        self.one = one
        self.two = two
        self.prev = prev


# O(n) time | O(h) space, h --> height of the tree
def repairBst(tree):
    info = Info()
    stack = []
    node = tree
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if info.prev and info.prev.value > node.value:
            if info.one is None:
                info.one = info.prev
            info.two = node
        info.prev = node
        node = node.right
    info.one.value, info.two.value = info.two.value, info.one.value
    return tree


