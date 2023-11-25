# https://www.algoexpert.io/questions/find-three-largest-numbers

# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    res = [None] * 3
    for value in array:
        insert(res, value)
    return res


def insert(res, value):
    for i in reversed(range(3)):
        if res[i] == None:
            res[i] = value
            break
        if value < res[i]:
            continue
        for j in range(i):
            res[j] = res[j + 1]
        res[i] = value
        break
