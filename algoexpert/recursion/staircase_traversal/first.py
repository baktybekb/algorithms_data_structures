# O(n * k) time | O(n) space
def staircaseTraversal(height, maxSteps):
    result = [0] * (height + 1)
    result[0] = result[1] = 1
    for i in range(2, height + 1):
        start_idx = max(i - maxSteps, 0)
        current_ways = 0
        for j in range(start_idx, i):
            current_ways += result[j]
        result[i] = current_ways
    return result[-1]
