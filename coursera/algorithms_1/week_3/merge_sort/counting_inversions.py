"""
Problem:
    An inversion in an array a[] is a pair of entries a[i] and a[j] such that i < j but a[i] > a[j].
    Given an array, design a linearithmic algorithm to count the number of inversions.
"""


def count_inversions(array):
    if len(array) <= 1:
        return array
    auxiliary = array[:]
    return helper(array, 0, len(array) - 1, auxiliary)


def do_merge(array, start, mid, end, auxiliary):
    i = k = start
    j = mid + 1
    inversions = 0
    while i <= mid and j <= end:
        if auxiliary[i] <= auxiliary[j]:
            array[k] = auxiliary[i]
            i += 1
        else:
            array[k] = auxiliary[j]
            j += 1
            inversions += mid - i + 1
        k += 1
    while i <= mid:
        array[k] = auxiliary[i]
        i += 1
        k += 1
    while j <= end:
        array[k] = auxiliary[j]
        j += 1
        k += 1
    return inversions


def helper(array, start, end, auxiliary):
    if start >= end:
        return 0
    mid = (start + end) // 2
    left = helper(auxiliary, start, mid, array)
    right = helper(auxiliary, mid + 1, end, array)
    return left + right + do_merge(array, start, mid, end, auxiliary)


def test():
    data = [4, 6, 1, 8, 2, 9, 5]
    assert count_inversions(data) == 8


if __name__ == '__main__':
    test()
