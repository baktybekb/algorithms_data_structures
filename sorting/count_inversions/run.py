# O(nlog(n)) time | O(n) space
def countInversions(array):
    if len(array) <= 1:
        return 0
    auxiliary = array[:]
    return helper(array, 0, len(array) - 1, auxiliary)


def helper(array, start, end, auxiliary):
    if start == end:
        return 0
    mid = (start + end) // 2
    left = helper(auxiliary, start, mid, array)
    right = helper(auxiliary, mid + 1, end, array)
    return left + right + do_merge(array, start, mid, end, auxiliary)


def do_merge(array, start, mid, end, auxiliary):
    k = start
    i = start
    j = mid + 1
    inversions = 0
    while i <= mid and j <= end:
        if auxiliary[i] <= auxiliary[j]:
            array[k] = auxiliary[i]
            i += 1
        else:
            array[k] = auxiliary[j]
            inversions += mid - i + 1
            j += 1
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
