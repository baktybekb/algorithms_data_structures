from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {i: [] for i in range(numCourses)}
        for i in prerequisites:
            first, second = i
            course_map[first].append(second)
        visited = set()

        def dfs(idx):
            if idx in visited:
                return False
            if not course_map[idx]:
                return True
            visited.add(idx)
            for pre in course_map[idx]:
                if not dfs(pre):
                    return False
            visited.remove(idx)
            course_map[idx] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
