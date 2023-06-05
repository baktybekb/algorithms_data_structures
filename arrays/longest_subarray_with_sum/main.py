# O(n) time | O(1) space
def longestSubarrayWithSum(array, target_sum):
    indeces = []
    start_idx = end_idx = cur_sum = 0
    while end_idx < len(array):
        cur_sum += array[end_idx]
        while start_idx < end_idx and cur_sum > target_sum:
            cur_sum -= array[start_idx]
            start_idx += 1
        if cur_sum == target_sum:
            if not indeces or indeces[1] - indeces[0] < end_idx - start_idx:
                indeces = [start_idx, end_idx]
        end_idx += 1
    return indeces
