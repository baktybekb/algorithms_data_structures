# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, prev=None, node1=None, node2=None):
        self.prev = prev
        self.node1 = node1
        self.node2 = node2

# O(n) time | O(h) space, h --> height of the tree, recursive call stack
def repairBst(tree):
    tree_info = TreeInfo()
    in_order(tree, tree_info)
    tree_info.node1.value, tree_info.node2.value = tree_info.node2.value, tree_info.node1.value
    return tree

def in_order(node, tree_info):
    if node is None:
        return
    in_order(node.left, tree_info)
    if tree_info.prev and tree_info.prev.value > node.value:
        if tree_info.node1 is None:
            tree_info.node1 = tree_info.prev
        tree_info.node2 = node
    tree_info.prev = node
    in_order(node.right, tree_info)
    return node
