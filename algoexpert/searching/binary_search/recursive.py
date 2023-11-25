# https://www.algoexpert.io/questions/binary-search

# O(log(n)) time | O(log(n)) space
def binarySearch(array, target):
    return helper(array, 0, len(array) - 1, target)


def helper(array, start, end, target):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] < target:
        return helper(array, mid + 1, end, target)
    elif array[mid] > target:
        return helper(array, start, mid - 1, target)
    else:
        return mid

