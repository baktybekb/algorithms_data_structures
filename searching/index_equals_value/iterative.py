# O(log(n)) time | O(1) space
def indexEqualsValue(array):
    return helper(0, len(array) - 1, array)


def helper(left, right, array):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == mid:
            if mid == 0 or array[mid - 1] != mid - 1:
                return mid
            right = mid - 1
        elif array[mid] < mid:
            left = mid + 1
        elif array[mid] > mid:
            right = mid - 1
    return -1
