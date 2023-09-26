# https://www.algoexpert.io/questions/zero-sum-subarray

# O(n) time | O(1) space
def zeroSumSubarray(nums):
    sums = set()
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum in sums or current_sum == 0:
            return True
        sums.add(current_sum)
    return False


if __name__ == '__main__':
    zeroSumSubarray([2, -2])
