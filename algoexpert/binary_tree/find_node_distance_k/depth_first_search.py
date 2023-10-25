# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def findNodesDistanceK(tree, target, k):
    visited, data = set(), []

    def helper(node):
        if node is None:
            return
        if target == node.value:
            traverse_down(node, 0, k, data, visited)
            return 1
        left = helper(node.left)
        right = helper(node.right)
        if left == k or right == k:
            data.append(node.value)
            return
        if left:
            traverse_down(node, left, k, data, visited)
            return left + 1
        if right:
            traverse_down(node, right, k, data, visited)
            return right + 1

    helper(tree)
    return data


def traverse_down(node, distance, k, data, visited):
    if node is None or node.value in visited:
        return
    visited.add(node.value)
    if distance == k:
        data.append(node.value)
        return
    distance += 1
    traverse_down(node.left, distance, k, data, visited)
    traverse_down(node.right, distance, k, data, visited)


