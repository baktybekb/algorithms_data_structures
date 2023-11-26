# https://www.algoexpert.io/questions/index-equals-value

# O(log(n)) time | O(log(n)) space
def indexEqualsValue(array):
    return search(array, 0, len(array) - 1, -1)


def search(array, l, r, value):
    if l > r:
        return value
    mid = (l + r) // 2
    if mid < array[mid]:
        return search(array, l, mid - 1, value)
    elif mid > array[mid]:
        return search(array, mid + 1, r, value)
    else:
        return search(array, l, mid - 1, mid)
