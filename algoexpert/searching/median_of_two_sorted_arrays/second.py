# O(log(min(n, m))) time | O(1) space
def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    small_array = arrayOne if len(arrayOne) <= len(arrayTwo) else arrayTwo
    big_array = arrayOne if len(arrayOne) >= len(arrayTwo) else arrayTwo
    left = 0
    right = len(small_array) - 1
    target = (len(small_array) + len(big_array) - 1) // 2
    while True:
        partition = (left + right) // 2
        big_partition = target - partition - 1

        small_left_max = small_array[partition] if partition >= 0 else float('-inf')
        small_right_min = small_array[partition + 1] if partition + 1 < len(small_array) else float('inf')
        big_left_max = big_array[big_partition] if big_partition >= 0 else float('-inf')
        big_right_min = big_array[big_partition + 1] if big_partition + 1 < len(big_array) else float('inf')

        if small_left_max > big_right_min:
            right = partition - 1
        elif big_left_max > small_right_min:
            left = partition + 1
        else:
            if (len(small_array) + len(big_array)) % 2 == 0:
                return (max(small_left_max, big_left_max) + min(small_right_min, big_right_min)) / 2
            return max(small_left_max, big_left_max)


if __name__ == '__main__':
    res = medianOfTwoSortedArrays(arrayOne=[1], arrayTwo=[2, 3, 9])
    assert res == 2.5
