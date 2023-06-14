# O(nlog(n)) time | O(log(n)) space
def quickSort(array):
    helper(array, 0, len(array) - 1)
    return array


def helper(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(array, left, right)
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]:
            right -= 1
    swap(array, pivot, right)
    left_is_smaller = right - 1 - start < end - (right + 1)
    if left_is_smaller:
        helper(array, start, right - 1)
        helper(array, right + 1, end)
    else:
        helper(array, right + 1, end)
        helper(array, start, right - 1)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
