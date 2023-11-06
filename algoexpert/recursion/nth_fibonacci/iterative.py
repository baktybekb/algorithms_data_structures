# https://www.algoexpert.io/questions/nth-fibonacci

# O(n) time | O(1) space
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    prev = 0
    cur = 1
    for i in range(2, n):
        temp = cur
        cur = prev + cur
        prev = temp
    return cur
