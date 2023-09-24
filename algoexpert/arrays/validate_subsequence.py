# https://www.algoexpert.io/questions/validate-subsequence

# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    idx = 0
    for num in array:
        if idx == len(sequence):
            break
        if sequence[idx] == num:
            idx += 1
    return idx == len(sequence)

