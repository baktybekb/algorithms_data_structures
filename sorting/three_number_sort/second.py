# O(n) time | O(1) space
def threeNumberSort(array, order):
    start = 0
    for i in range(len(array)):
        if array[i] == order[0]:
            swap(array, i, start)
            start += 1
    end = len(array) - 1
    for i in reversed(range(len(array))):
        if array[i] == order[2]:
            swap(array, i, end)
            end -= 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
