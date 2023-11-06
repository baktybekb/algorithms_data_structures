# O(n * k) time | O(n) space
def staircaseTraversal(height, maxSteps):
    res = [0] * (height + 1)
    res[0] = res[1] = 1
    for i in range(2, height + 1):
        cur_sum = 0
        for j in range(i - min(height, maxSteps), i):
            cur_sum += res[j]
        res[i] = cur_sum
    return res[-1]
