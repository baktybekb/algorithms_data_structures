# O(n) time | O(1) space
def longestSubarrayWithSum(array, target_sum):
    res = []
    l = cur_sum = 0
    for r in range(len(array)):
        cur_sum += array[r]
        while cur_sum > target_sum and l < r:
            cur_sum -= array[l]
            l += 1
        if cur_sum != target_sum:
            continue
        length = (res[1] - res[0]) if res else -1
        if r - l <= length:
            continue
        res = [l, r]
    return res


if __name__ == '__main__':
    assert longestSubarrayWithSum([1, 2, 3, 4, 3, 3, 1, 2, 1], 10) == [4, 8]
    assert longestSubarrayWithSum([0], 0) == [0, 0]

