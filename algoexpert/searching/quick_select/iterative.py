# https://www.algoexpert.io/questions/quickselect

# O(n) time | O(1) space
def quickselect(array, k):
    return helper(0, len(array) - 1, array, k - 1)


def helper(start, end, array, k):
    while start < end:
        pivot = start
        l, r = start + 1, end
        while l <= r:
            if array[r] < array[pivot] < array[l]:
                swap(l, r, array)
            if array[l] <= array[pivot]:
                l += 1
            if array[r] >= array[pivot]:
                r -= 1
        swap(pivot, r, array)
        if r == k:
            return array[r]
        if k < r:
            end = r - 1
        else:
            start = r + 1
    return array[start]


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


