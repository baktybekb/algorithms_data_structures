# https://www.algoexpert.io/questions/search-for-range

# O(log(n)) time | O(log(n)) space
def searchForRange(array, target):
    final_range = [-1, -1]
    search(array, 0, len(array) - 1, target, final_range, True)
    search(array, 0, len(array) - 1, target, final_range, False)
    return final_range


def search(array, left, right, target, final_range, go_left):
    if left > right:
        return
    mid = (left + right) // 2
    if array[mid] < target:
        search(array, mid + 1, right, target, final_range, go_left)
    elif array[mid] > target:
        search(array, left, mid - 1, target, final_range, go_left)
    else:
        if go_left:
            if mid == 0 or array[mid - 1] != target:
                final_range[0] = mid
                return
            search(array, left, mid - 1, target, final_range, go_left)
        else:
            if mid == len(array) - 1 or array[mid + 1] != target:
                final_range[1] = mid
                return
            search(array, mid + 1, right, target, final_range, go_left)
