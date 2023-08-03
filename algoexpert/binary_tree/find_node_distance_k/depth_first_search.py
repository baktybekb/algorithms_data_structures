# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def findNodesDistanceK(tree, target, k):
    array = []
    dfs(tree, target, k, array)
    return array


def dfs(node, target, k, array):
    if node is None:
        return -1
    if node.value == target:
        traverse_tree(node, 0, k, array)
        return 1
    left = dfs(node.left, target, k, array)
    right = dfs(node.right, target, k, array)
    if left == k or right == k:
        array.append(node.value)
        return -1
    elif left == right == -1:
        return -1
    else:
        if left > 0:
            traverse_tree(node.right, left + 1, k, array)
            return left + 1
        else:
            traverse_tree(node.left, right + 1, k, array)
            return right + 1


def traverse_tree(node, distance, k, array):
    if node is None:
        return
    if distance == k:
        array.append(node.value)
        return
    distance += 1
    traverse_tree(node.left, distance, k, array)
    traverse_tree(node.right, distance, k, array)

