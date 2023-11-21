# O(n) time | O(1) space
def threeNumberSort(array, order):

    def traverse(index, step, range_obj, order_val):
        for i in range_obj:
            if array[i] == order_val:
                swap(i, index, array)
                index += step

    length = len(array)
    traverse(0, 1, range(length), order[0])
    traverse(length - 1, -1, reversed(range(length)), order[2])
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
