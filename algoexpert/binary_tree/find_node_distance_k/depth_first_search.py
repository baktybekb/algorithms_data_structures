# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def findNodesDistanceK(tree, target, k):
    array = []
    dfs(tree, array, target, k)
    return array


def dfs(node, array, target, k):
    if node is None:
        return -1
    if node.value == target:
        traverse_subtree(node, array, k)
        return 1
    left = dfs(node.left, array, target, k)
    right = dfs(node.right, array, target, k)
    if left == k or right == k:
        array.append(node.value)
    if left != -1:
        traverse_subtree(node.right, array, k, depth=left + 1)
        return left + 1
    if right != -1:
        traverse_subtree(node.left, array, k, depth=right + 1)
        return right + 1
    return -1


def traverse_subtree(node, array, k, depth=0):
    if node is None:
        return
    if depth == k:
        array.append(node.value)
    else:
        traverse_subtree(node.left, array, k, depth + 1)
        traverse_subtree(node.right, array, k, depth + 1)
