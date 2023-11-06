# https://www.algoexpert.io/questions/staircase-traversal

# O(n) time | O(n) space
def staircaseTraversal(height, maxSteps):
    res = [0] * (height + 1)
    res[0] = 1
    l, cur_sum = 0, 1
    for r in range(1, height + 1):
        res[r] = cur_sum

        # computation for the next iteration
        window_start = max(r - maxSteps + 1, 0)
        cur_sum += res[r]
        if window_start == l:
            continue
        cur_sum -= res[l]
        l += 1
    return res[-1]


if __name__ == '__main__':
    staircaseTraversal(5, 2)
