# https://www.algoexpert.io/questions/subarray-sort

# O(n) time | O(1) space
def subarraySort(array):
    small, big = float('inf'), float('-inf')
    for i in range(len(array) - 1):
        if array[i] <= array[i + 1]:
            continue
        small = min(small, array[i + 1])
        big = max(big, array[i])
    res = [0, 0]
    l, r = 0, len(array) - 1
    while l <= r and array[l] <= small:
        l += 1
    res[0] = -1 if l > r else l
    while r >= 0 and big <= array[r]:
        r -= 1
    res[1] = -1 if r < 0 else r
    return res


if __name__ == '__main__':
    assert subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]) == [3, 9]
