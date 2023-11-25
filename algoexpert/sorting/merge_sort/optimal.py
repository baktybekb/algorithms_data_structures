# https://www.algoexpert.io/questions/merge-sort

# O(nlog(n)) time | O(n) space
def mergeSort(array):
    auxiliary = array.copy()
    do_merge(array, auxiliary, 0, len(array) - 1)
    return array


def do_merge(array, auxiliary, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    do_merge(auxiliary, array, start, mid)
    do_merge(auxiliary, array, mid + 1, end)
    i = k = start
    j = mid + 1
    while i <= mid and j <= end:
        if auxiliary[i] <= auxiliary[j]:
            array[k] = auxiliary[i]
            i += 1
        else:
            array[k] = auxiliary[j]
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

