# https://www.algoexpert.io/questions/single-cycle-check

# 1. we start from 0 index
# 2.if after traversing the array idx != 0 --> we must do only one cycle, and return to idx ==0
# 3. if 0 < i < len(array) and idx == 0 --> cycle during the loop

# O(n) time | O(1) space
def hasSingleCycle(array):
    dest_idx = 0
    for i in range(len(array)):
        if i > 0 and dest_idx == 0:
            return False
        step = array[dest_idx]
        dest_idx = (dest_idx + step) % len(array)
    return dest_idx == 0
