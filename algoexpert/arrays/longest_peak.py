# https://www.algoexpert.io/questions/longest-peak

# O(n) time | O(1) space
def longestPeak(array):
    longest = 0
    i = 1
    while i < len(array) - 1:
        if array[i - 1] < array[i] and array[i] > array[i + 1]:
            l = r = i
            length = 1
            while l - 1 >= 0 and array[l - 1] < array[l]:
                l -= 1
                length += 1
            while r + 1 < len(array) and array[r] > array[r + 1]:
                r += 1
                length += 1
            if length > longest:
                longest = length
            i = r
        else:
            i += 1
    return longest
