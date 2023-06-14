# O(nlog(n)) time | O(nlog(n)) space --> new sorted array
def mergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]
    return do_merge(mergeSort(left_half), mergeSort(right_half))


def do_merge(array_one, array_two):
    sorted_array = [0] * (len(array_one) + len(array_two))
    i = j = k = 0
    while i < len(array_one) and j < len(array_two):
        if array_one[i] <= array_two[j]:
            sorted_array[k] = array_one[i]
            i += 1
        else:
            sorted_array[k] = array_two[j]
            j += 1
        k += 1
    while i < len(array_one):
        sorted_array[k] = array_one[i]
        i += 1
        k += 1
    while j < len(array_two):
        sorted_array[k] = array_two[j]
        j += 1
        k += 1
    return sorted_array


if __name__ == '__main__':
    data = [8, 5, 2, 9, 5, 6, 3]
    res = mergeSort(data)
    print(res)
