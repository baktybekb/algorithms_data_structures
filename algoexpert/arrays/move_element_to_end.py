# https://www.algoexpert.io/questions/move-element-to-end

# O(n) time | O(1) space
def moveElementToEnd(array, to_move):
    l, r = 0, len(array) - 1
    while l < r:
        while l < r and array[r] == to_move:
            r -= 1
        while l < r and array[l] != to_move:
            l += 1
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1
    return array
