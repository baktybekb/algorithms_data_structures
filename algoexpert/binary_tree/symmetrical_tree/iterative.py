# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space
def symmetricalTree(tree):
    left_stack = [tree.left]
    right_stack = [tree.right]
    while left_stack and right_stack:
        left_node = left_stack.pop()
        right_node = right_stack.pop()
        if not left_node and not right_node:
            continue
        if not left_node or not right_node or left_node.value != right_node.value:
            return False
        left_stack.append(left_node.left)
        right_stack.append(right_node.right)

        left_stack.append(left_node.right)
        right_stack.append(right_node.left)
    return True
