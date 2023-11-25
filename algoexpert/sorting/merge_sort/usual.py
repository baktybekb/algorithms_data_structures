# https://www.algoexpert.io/questions/merge-sort

# O(nlog(n)) time | O(nlog(n)) space
def mergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left, right = array[:mid], array[mid:]
    return do_merge(
        mergeSort(left), mergeSort(right)
    )


def do_merge(array_one, array_two):
    merged = []
    i = j = 0
    while i < len(array_one) and j < len(array_two):
        if array_one[i] <= array_two[j]:
            merged.append(array_one[i])
            i += 1
        else:
            merged.append(array_two[j])
            j += 1
    while i < len(array_one):
        merged.append(array_one[i])
        i += 1
    while j < len(array_two):
        merged.append(array_two[j])
        j += 1
    return merged
