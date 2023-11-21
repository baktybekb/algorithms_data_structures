# https://www.algoexpert.io/questions/quick-sort

# O(nlog(n)) time | O(log(n)) space
# worst case: O(n^2) time | O(n) space
def quickSort(array):
    helper(0, len(array) - 1, array)
    return array


def helper(start, end, array):
    if start >= end:
        return
    pivot = start
    l = start + 1
    r = end
    while l <= r:
        if array[l] > array[pivot] > array[r]:
            swap(l, r, array)
        if array[l] <= array[pivot]:
            l += 1
        if array[pivot] <= array[r]:
            r -= 1
    swap(pivot, r, array)
    if r - start <= end - r:
        helper(start, r - 1, array)
        helper(r + 1, end, array)
    else:
        helper(r + 1, end, array)
        helper(start, r - 1, array)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
