# https://www.algoexpert.io/questions/shifted-binary-search

# O(log(n)) time | O(log(n)) space
def shiftedBinarySearch(array, target):
    return helper(0, len(array) - 1, array, target)


def helper(l, r, array, target):
    if l > r:
        return -1
    mid = (l + r) // 2
    if array[mid] == target:
        return mid
    if array[l] <= array[mid]:
        if array[l] <= target < array[mid]:
            return helper(l, mid - 1, array, target)
        return helper(mid + 1, r, array, target)
    else:
        if array[mid] < target <= array[r]:
            return helper(mid + 1, r, array, target)
        return helper(l, mid - 1, array, target)
