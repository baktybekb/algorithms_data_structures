# https://www.algoexpert.io/questions/staircase-traversal

# O(k * n) time | O(n) space
def staircaseTraversal(height, maxSteps):
    height_map = {}

    def helper(height):
        if height in height_map:
            return height_map[height]
        if height <= 1:
            height_map[1] = 1
            return 1
        total = 0
        for i in range(1, min(height, maxSteps) + 1):
            total += helper(height - i)
        height_map[height] = total
        return total

    return helper(height)


if __name__ == '__main__':
    staircaseTraversal(10, 2)

