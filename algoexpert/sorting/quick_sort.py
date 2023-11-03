# https://www.algoexpert.io/questions/quick-sort

# O(nlog(n)) time | O(log(n)) space
def quickSort(array):
    helper(0, len(array) - 1, array)
    return array


def helper(start, end, array):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        if array[right] < array[pivot] < array[left]:
            swap(left, right, array)
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]:
            right -= 1
    swap(pivot, right, array)
    if right - start > end - right:
        helper(start, right - 1, array)
        helper(right + 1, end, array)
    else:
        helper(right + 1, end, array)
        helper(start, right - 1, array)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

