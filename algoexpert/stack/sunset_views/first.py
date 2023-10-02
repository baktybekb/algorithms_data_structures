# https://www.algoexpert.io/questions/sunset-views

# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    stack = []
    range_ = range(len(buildings))
    direction_range = range_ if direction == 'EAST' else reversed(range_)
    for i in direction_range:
        while stack and buildings[stack[-1]] <= buildings[i]:
            stack.pop()
        stack.append(i)
    return stack if direction == 'EAST' else swap(stack)


# O(n) time | O(1) space
def swap(array):
    l, r = 0, len(array) - 1
    while l < r:
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1
    return array
