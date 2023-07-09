# sliding window
def staircaseTraversal(height, maxSteps):
    current_ways = 0
    data = [1]
    for current_height in range(1, height + 1):
        window_start = current_height - maxSteps - 1
        window_end = current_height - 1
        if window_start >= 0:
            current_ways -= data[window_start]
        current_ways += data[window_end]
        data.append(current_ways)
    return current_ways
