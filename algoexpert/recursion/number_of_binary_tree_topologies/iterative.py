# O(n^2) time | O(n) space
def numberOfBinaryTreeTopologies(n):
    cache = [1]
    for size in range(1, n + 1):
        cur_top = 0
        for left_size in range(size):
            right_size = size - 1 - left_size
            left_top = cache[left_size]
            right_top = cache[right_size]
            cur_top += left_top * right_top
        cache.append(cur_top)
    return cache[n]
