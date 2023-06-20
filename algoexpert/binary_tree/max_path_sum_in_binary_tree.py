# O(n) time | O(log(n)) average case, where binary tree is balanced
# O(n) time | O(n) worst case, where tree like a linked list
def maxPathSum(tree):
    branch_sum, max_path = helper(tree)
    return max(branch_sum, max_path)


def helper(node):
    if node is None:
        return float('-inf'), float('-inf')
    left_sum_as_branch, left_sum = helper(node.left)
    right_sum_as_branch, right_sum = helper(node.right)
    max_child_sum_as_branch = max(left_sum_as_branch, right_sum_as_branch)
    max_current_sum_as_branch = max(max_child_sum_as_branch + node.value, node.value)
    max_sum_as_root = max(max_current_sum_as_branch, left_sum_as_branch + right_sum_as_branch + node.value)
    max_path_sum = max(max_sum_as_root, left_sum, right_sum)
    return max_current_sum_as_branch, max_path_sum
