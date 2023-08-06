from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        white - 0 not visited
        grey  - 1 currently in a process
        black - 2 finished process, do not have cycle
        """
        course_map = {i: [] for i in range(numCourses)}
        for i in prerequisites:
            first, second = i
            course_map[first].append(second)
        stack = [0] * numCourses

        def dfs(idx):
            stack[idx] = 1
            for pre in course_map[idx]:
                if stack[pre] == 0:
                    if not dfs(pre):
                        return False
                elif stack[pre] == 1:
                    return False
                else:
                    continue
            stack[idx] = 2
            return True

        for idx in range(numCourses):
            if not dfs(idx):
                return False
        return True
