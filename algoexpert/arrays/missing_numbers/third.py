# O(n) time | O(n) space
def missingNumbers(nums):
    xor_missing = 0
    for i in range(len(nums) + 3):
        xor_missing ^= i
        if i < len(nums):
            xor_missing ^= nums[i]
    solution = [0, 0]
    rightmost_bit = xor_missing & -xor_missing
    for i in range(len(nums) + 3):
        if rightmost_bit & i == 0:
            solution[0] ^= i
        else:
            solution[1] ^= i
        if i < len(nums):
            if rightmost_bit & nums[i] == 0:
                solution[0] ^= nums[i]
            else:
                solution[1] ^= nums[i]
    return sorted(solution)


if __name__ == '__main__':
    assert missingNumbers([1, 4, 3]) == [2, 5]
    assert missingNumbers([4, 5, 1, 3]) == [2, 6]
