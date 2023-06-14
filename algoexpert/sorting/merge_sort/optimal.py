# O(nlog(n)) time | O(n) space --> inplace sorting
def mergeSort(array):
    if len(array) == 1:
        return array
    auxiliary = array[:]
    helper(array, 0, len(array) - 1, auxiliary)
    return array


def helper(array, start, end, auxiliary):
    if start == end:
        return
    mid = (start + end) // 2
    helper(auxiliary, start, mid, array)
    helper(auxiliary, mid + 1, end, array)
    do_merge(array, start, mid, end, auxiliary)


def do_merge(array, start, mid, end, auxiliary):
    k = start
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if auxiliary[i] <= auxiliary[j]:
            array[k] = auxiliary[i]
            i += 1
            k += 1
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


if __name__ == '__main__':
    data = [8, 5, 2, 9, 5, 6, 3]
    mergeSort(data)
    print(data)
