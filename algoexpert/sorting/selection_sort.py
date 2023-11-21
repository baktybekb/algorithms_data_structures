# https://www.algoexpert.io/questions/selection-sort

# O(n^2) time | O(1) space
def selectionSort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        swap(min_idx, i, array)
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
