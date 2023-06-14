# O(n^2) time | O(1) space
def selectionSort(array):
    for i in range(len(array) - 1):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] >= array[min_idx]:
                continue
            min_idx = j
        if min_idx == i:
            continue
        swap(array, i, min_idx)
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
