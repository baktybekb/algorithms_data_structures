# https://leetcode.com/problems/teemo-attacking/description/

from typing import List


# O(n) time | O(1) space
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count, last_time = 0, None
        for time in timeSeries:
            desired = time + duration - 1
            if last_time and time <= last_time:
                diff = desired - last_time
            else:
                diff = duration
            count += diff
            last_time = desired
        return count


if __name__ == '__main__':
    sol = Solution()
    assert sol.findPoisonedDuration(timeSeries=[1, 2], duration=2) == 3
    assert sol.findPoisonedDuration(timeSeries=[1, 4], duration=2) == 4
