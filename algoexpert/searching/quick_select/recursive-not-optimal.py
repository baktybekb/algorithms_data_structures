# O(n) time | O(log(n)) space
def quickselect(array, k):
    return helper(0, len(array) - 1, array, k - 1)


def helper(start, end, array, k):
    if start >= end:
        return array[start]
    pivot = start
    l = start + 1
    r = end
    while l <= r:
        if array[r] < array[pivot] < array[l]:
            swap(l, r, array)
        if array[l] <= array[pivot]:
            l += 1
        if array[r] >= array[pivot]:
            r -= 1
    swap(pivot, r, array)
    if r == k:
        return array[k]
    if k < r:
        return helper(start, r - 1, array, k)
    return helper(r + 1, end, array, k)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

