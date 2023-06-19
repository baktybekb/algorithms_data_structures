# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(node):
    if node.value > 0:
        return node.value
    left = evaluateExpressionTree(node.left)
    right = evaluateExpressionTree(node.right)
    if node.value == -1:
        return left + right
    elif node.value == -2:
        return left - right
    elif node.value == -3:
        return int(left / right)
    return left * right



