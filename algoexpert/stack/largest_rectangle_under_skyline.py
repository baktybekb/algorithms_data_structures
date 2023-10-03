# O(n) time | O(n) space
def largestRectangleUnderSkyline(buildings):
    stack = []
    max_area = 0
    for i, hei in enumerate(buildings):
        start = i
        while stack and stack[-1][1] > hei:
            idx, prev_hei = stack.pop()
            max_area = max(max_area, (i - idx) * prev_hei)
            start = idx
        stack.append((start, hei))
    while stack:
        i, hei = stack.pop()
        max_area = max(max_area, (len(buildings) - i) * hei)
    return max_area


if __name__ == '__main__':
    assert largestRectangleUnderSkyline([1, 3, 3, 2, 4, 1, 5, 3, 2]) == 9
