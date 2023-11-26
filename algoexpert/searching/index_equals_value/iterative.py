# https://www.algoexpert.io/questions/index-equals-value

# O(log(n)) time | O(1) space
def indexEqualsValue(array):
    l, r = 0, len(array) - 1
    value = -1
    while l <= r:
        mid = (l + r) // 2
        if mid < array[mid]:
            r = mid - 1
        elif mid > array[mid]:
            l = mid + 1
        else:
            value = mid
            r = mid - 1
    return value

