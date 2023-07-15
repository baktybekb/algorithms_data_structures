# O(n + m) time | O(1) space
def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    i = j = 0
    target_idx = (len(arrayOne) + len(arrayTwo) - 1) // 2
    while i + j < target_idx:
        if i >= len(arrayOne):
            j += 1
        elif j >= len(arrayTwo):
            i += 1
        elif arrayOne[i] <= arrayTwo[j]:
            i += 1
        else:
            j += 1

    if (len(arrayOne) + len(arrayTwo)) % 2 == 0:
        both_in_one = j >= len(arrayTwo) or (i + 1 < len(arrayOne) and arrayOne[i + 1] <= arrayTwo[j])
        both_in_two = i >= len(arrayOne) or (j + 1 < len(arrayTwo) and arrayTwo[j + 1] <= arrayOne[i])
        value_one = arrayTwo[j + 1] if both_in_two else arrayOne[i]
        value_two = arrayOne[i + 1] if both_in_one else arrayTwo[j]
        return (value_one + value_two) / 2

    value_one = arrayOne[i] if i < len(arrayOne) else float('inf')
    value_two = arrayTwo[j] if j < len(arrayTwo) else float('inf')
    return min(value_one, value_two)


if __name__ == '__main__':
    res = medianOfTwoSortedArrays(arrayOne=[1], arrayTwo=[2, 3, 9])
    assert res == 2.5



