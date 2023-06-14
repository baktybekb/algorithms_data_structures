# O(n) time | O(1) space
def threeNumberSort(array, order):
    first = second = 0
    third = len(array) - 1
    while second <= third:
        if array[second] == order[1]:
            second += 1
        elif array[second] == order[0]:
            swap(array, first, second)
            first += 1
            second += 1
        elif array[second] == order[2]:
            swap(array, second, third)
            third -= 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
