# https://www.algoexpert.io/questions/merge-overlapping-intervals

# O(nlog(n)) time | O(n) space
def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    stack = []
    for start, end in intervals:
        if not stack:
            stack.append([start, end])
        else:
            prev_start, prev_end = stack[-1]
            if start <= prev_end:
                stack[-1][1] = max(prev_end, end)
            else:
                stack.append([start, end])
    return stack

