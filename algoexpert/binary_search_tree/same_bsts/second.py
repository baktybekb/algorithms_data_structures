# https://www.algoexpert.io/questions/same-bsts

# O(n^2) time | O(h) space, h --> height of the tree
def sameBsts(array_one, array_two):
    def helper(idx_one, idx_two, min_val, max_val):
        if idx_one == -1 or idx_two == -1:
            return idx_one == idx_two
        if array_one[idx_one] != array_two[idx_two]:
            return False
        value = array_one[idx_one]
        left_idx_one = get_left_tree(array_one, idx_one, min_val)
        right_idx_one = get_right_tree(array_one, idx_one, max_val)

        left_idx_two = get_left_tree(array_two, idx_two, min_val)
        right_idx_two = get_right_tree(array_two, idx_two, max_val)
        return (
            helper(left_idx_one, left_idx_two, min_val, value) and
            helper(right_idx_one, right_idx_two, value, max_val)
        )

    return helper(0, 0, float('-inf'), float('inf'))


def get_left_tree(array, prev_idx, min_val):
    root_idx = -1
    for i in range(prev_idx + 1, len(array)):
        if min_val <= array[i] < array[prev_idx]:
            root_idx = i
            break
    return root_idx


def get_right_tree(array, prev_idx, max_val):
    root_idx = -1
    for i in range(prev_idx + 1, len(array)):
        if array[prev_idx] <= array[i] < max_val:
            root_idx = i
            break
    return root_idx











