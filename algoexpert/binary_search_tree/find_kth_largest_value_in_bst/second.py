# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, visited_count, last_visited_number):
        self.visited_count = visited_count
        self.last_visited_number = last_visited_number

# O(h + k) time | O(h) space --> h - height
def findKthLargestValueInBst(tree, k):
    tree_info = TreeInfo(0, -1)
    reverse_inorder_traverse(tree, tree_info, k)
    return tree_info.last_visited_number


def reverse_inorder_traverse(node, tree_info, k):
    if node is None or tree_info.visited_count == k:
        return
    reverse_inorder_traverse(node.right, tree_info, k)
    if tree_info.visited_count < k:
        tree_info.visited_count += 1
        tree_info.last_visited_number = node.value
        reverse_inorder_traverse(node.left, tree_info, k)
