# O(n^2) time | O(h) space, h --> height of bst
def sameBsts(arrayOne, arrayTwo):
    return helper(arrayOne, arrayTwo, 0, 0, float('-inf'), float('inf'))


def helper(array_one, array_two, root_idx_one, root_idx_two, min_val, max_val):
    if root_idx_one == -1 or root_idx_two == -1:
        return root_idx_one == root_idx_two
    if array_one[root_idx_one] != array_two[root_idx_two]:
        return False
    left_idx_one = get_smaller(array_one, root_idx_one, min_val)
    left_idx_two = get_smaller(array_two, root_idx_two, min_val)
    right_idx_one = get_smaller(array_one, root_idx_one, max_val)
    right_idx_two = get_smaller(array_two, root_idx_two, max_val)
    current = array_one[root_idx_one]
    left_same = helper(array_one, array_two, left_idx_one, left_idx_two, min_val, current)
    right_same = helper(array_one, array_two, right_idx_one, right_idx_two, current, max_val)
    return left_same and right_same


def get_smaller(array, root_idx, min_val):
    for i in range(root_idx + 1, len(array)):
        if min_val <= array[i] < array[root_idx]:
            return i
    return -1


def get_greater(array, root_idx, max_val):
    for i in range(root_idx + 1, len(array)):
        if array[root_idx] <= array[i] < max_val:
            return i
    return -1
