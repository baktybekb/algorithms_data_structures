from typing import List
import collections


# O(n) time | O(n) space
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])
            if r - l + 1 != k:
                continue
            res.append(queue[0])
            if nums[l] == queue[0]:
                queue.popleft()
            l += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxSlidingWindow(nums=[8, 7, 6, 9], k=2) == [8, 7, 9]
    assert sol.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3) == [3, 3, 5, 5, 6, 7]
    assert sol.maxSlidingWindow(nums=[1, 3, 1, 2, 0, 5], k=3) == [3, 3, 2, 5]
