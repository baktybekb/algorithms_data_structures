# https://www.algoexpert.io/questions/count-inversions

# O(nlog(n)) time | O(n) space
def countInversions(array):
    auxiliary = array.copy()
    inversions = [0]
    do_merge(array, auxiliary, 0, len(array) - 1, inversions)
    return inversions[0]


def do_merge(array, auxiliary, start, end, inversions):
    if start >= end:
        return
    mid = (start + end) // 2
    do_merge(auxiliary, array, start, mid, inversions)
    do_merge(auxiliary, array, mid + 1, end, inversions)
    i = k = start
    j = mid + 1
    while i <= mid and j <= end:
        if auxiliary[i] <= auxiliary[j]:
            array[k] = auxiliary[i]
            i += 1
        else:
            array[k] = auxiliary[j]
            inversions[0] += mid - i + 1
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
