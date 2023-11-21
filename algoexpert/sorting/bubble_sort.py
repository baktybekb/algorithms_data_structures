# https://www.algoexpert.io/questions/bubble-sort

# O(n^2) time | O(1) space
def bubbleSort(array):
    is_sorted = False
    last_idx = len(array) - 1
    while not is_sorted:
        is_sorted = True
        for i in range(last_idx):
            if array[i] <= array[i + 1]:
                continue
            is_sorted = False
            swap(i, i + 1, array)
        last_idx -= 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
