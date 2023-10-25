# https://www.algoexpert.io/questions/merge-binary-trees

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n + m) time | O(n + m) space
def mergeBinaryTrees(tree1, tree2):
    stack = [(tree1, tree2)]
    while stack:
        node1, node2 = stack.pop()
        if node2 is None:
            continue
        if node1.left is None:
            node1.left = node2.left
        else:
            stack.append((node1.left, node2.left))
        if node1.right is None:
            node1.right = node2.right
        else:
            stack.append((node1.right, node2.right))
    return tree1

