# https://www.algoexpert.io/questions/insertion-sort

# O(n^2) time | O(1) space
# O(n) time - best case, where array is already sorted --> only one traversing
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(j, j - 1, array)
            j -= 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
