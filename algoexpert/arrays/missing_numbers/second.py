# O(n) time | O(n) space
def missingNumbers(nums):
    nums_set = set(nums)
    res = []
    for i in range(1, len(nums) + 3):
        if i not in nums_set:
            res.append(i)
    return res


if __name__ == '__main__':
    assert missingNumbers([1, 4, 3]) == [2, 5]

