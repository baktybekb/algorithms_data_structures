# O(log(n)) time | O(log(n)) space
def binarySearch(array, target):
    return helper(0, len(array) - 1, array, target)


def helper(left, right, array, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if array[mid] == target:
        return mid
    if array[mid] < target:
        return helper(mid + 1, right, array, target)
    else:
        return helper(left, mid - 1, array, target)
