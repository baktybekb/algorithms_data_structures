# O(log(n)) time | O(log(n)) space
def shiftedBinarySearch(array, target):
    return helper(0, len(array) - 1, array, target)


def helper(left, right, array, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if array[mid] == target:
        return mid
    if array[left] <= array[mid]:
        # left side is sorted
        if array[left] <= target < array[mid]:
            return helper(left, mid - 1, array, target)
        else:
            return helper(mid + 1, right, array, target)
    else:
        # left side is unsorted --> right side is sorted
        if array[mid] < target <= array[right]:
            return helper(mid + 1, right, array, target)
        else:
            return helper(left, mid - 1, array, target)




