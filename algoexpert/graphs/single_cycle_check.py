# O(n) time | O(1) space
def hasSingleCycle(array):
    visited = 0
    idx = 0
    while visited < len(array):
        if visited > 1 and idx == 0:
            return False
        idx = (idx + array[idx]) % len(array)
        visited += 1
    return idx == 0
