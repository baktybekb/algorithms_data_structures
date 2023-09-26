# https://www.algoexpert.io/questions/majority-element

# O(n) time | O(1) space
def majorityElement(array):
    majority = None
    count = 0
    for num in array:
        if count == 0:
            majority = num
            count = 1
        else:
            count += 1 if num == majority else -1
    return majority

