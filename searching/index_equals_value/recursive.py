# O(log(n)) time | O(log(n)) space
def indexEqualsValue(array):
    return helper(0, len(array) - 1, array)


def helper(left, right, array):
    if left > right:
        return -1
    mid = (left + right) // 2
    if array[mid] == mid:
        if mid == 0 or array[mid - 1] != mid - 1:
            return mid
        return helper(left, mid - 1, array)
    elif array[mid] < mid:
        return helper(mid + 1, right, array)
    elif array[mid] > mid:
        return helper(left, mid - 1, array)
