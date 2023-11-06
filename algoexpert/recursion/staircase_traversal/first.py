# https://www.algoexpert.io/questions/staircase-traversal

# O(k^n) time | O(n) space
# k = number of prev heights that could get to current height
def staircaseTraversal(height, maxSteps):
    if height <= 1:
        return 1
    total = 0
    for i in range(1, min(height, maxSteps) + 1):
        total += staircaseTraversal(height - i, maxSteps)
    return total


if __name__ == '__main__':
    staircaseTraversal(10, 2)

