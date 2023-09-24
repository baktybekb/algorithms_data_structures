# https://www.algoexpert.io/questions/two-number-sum

# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    hash_set = set()
    for num in array:
        diff = targetSum - num
        if diff in hash_set:
            return [diff, num]
        hash_set.add(num)
    return []
