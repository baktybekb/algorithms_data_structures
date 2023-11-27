# https://www.algoexpert.io/questions/median-of-two-sorted-arrays

# O(log(min(n, m))) time | O(1) space
def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    small = arrayOne if len(arrayOne) <= len(arrayTwo) else arrayTwo
    big = arrayOne if len(arrayOne) > len(arrayTwo) else arrayTwo
    total_length = len(small) + len(big)
    left, right = 0, len(small) - 1
    median_idx = (total_length - 1) // 2
    while True:
        small_mid = (left + right) // 2
        big_mid = median_idx - (small_mid + 1)

        small_left_max = small[small_mid] if small_mid >= 0 else float('-inf')
        small_right_min = small[small_mid + 1] if small_mid + 1 < len(small) else float('inf')
        big_left_max = big[big_mid] if big_mid >= 0 else float('-inf')
        big_right_min = big[big_mid + 1] if big_mid + 1 < len(big) else float('inf')

        if small_left_max > big_right_min:
            right = small_mid - 1
        elif big_left_max > small_right_min:
            left = small_mid + 1
        else:
            max_left = max(small_left_max, big_left_max)
            if total_length % 2 == 0:
                return (max_left + min(small_right_min, big_right_min)) / 2
            return max_left


if __name__ == '__main__':
    assert medianOfTwoSortedArrays([1, 3, 5, 6], [7, 8]) == 5.5
