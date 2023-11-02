from typing import List


# O(n) time | O(n) space
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        data = ((position[i], speed[i]) for i in range(len(position)))
        for pos, speed in sorted(data, key=lambda x: -x[0]):
            time = (target - pos) / speed
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)


if __name__ == '__main__':
    solution = Solution()
    assert solution.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]) == 3
