# O(n) time | O(1) space
def threeNumberSort(array, order):
    first = second = 0
    third = len(array) - 1
    while second <= third:
        if array[second] == order[0]:
            swap(first, second, array)
            first += 1
            second += 1
        elif array[second] == order[2]:
            swap(second, third, array)
            third -= 1
        else:
            second += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
