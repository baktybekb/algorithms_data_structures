def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j, j - 1)
            j -= 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
