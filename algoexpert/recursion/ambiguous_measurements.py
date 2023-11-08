# https://www.algoexpert.io/questions/ambiguous-measurements

# O(low * high * n) time | O(low * high) space
def ambiguousMeasurements(measuringCups, low, high):
    cache = {}
    return helper(measuringCups, low, high, cache)


def helper(measuring_cups, low, high, cache):
    key = f'{low}:{high}'
    if key in cache:
        return cache[key]
    if low <= 0 and high <= 0:
        return
    can_measure = False
    for cup_low, cup_high in measuring_cups:
        if low <= cup_low and cup_high <= high:
            can_measure = True
            break
        new_low = max(0, low - cup_low)
        new_high = max(0, high - cup_high)
        can_measure = helper(measuring_cups, new_low, new_high, cache)
        if can_measure:
            break
    cache[key] = can_measure
    return can_measure
