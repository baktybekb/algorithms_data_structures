import math

# https://www.algoexpert.io/questions/missingNumbers


# O(n) time | O(1) space
def missingNumbers(nums):
    desired = sum(range(1, len(nums) + 3))
    actual = sum(nums)
    diff = desired - actual
    partition = math.ceil(diff / 2)

    left_desired = sum(range(1, partition))
    right_desired = sum(range(partition, len(nums) + 3))

    left_actual = right_actual = 0
    for num in nums:
        if num < partition:
            left_actual += num
        else:
            right_actual += num
    return [
        left_desired - left_actual, right_desired - right_actual
    ]


if __name__ == '__main__':
    assert missingNumbers([1, 4, 3]) == [2, 5]

