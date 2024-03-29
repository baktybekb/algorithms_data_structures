# https://leetcode.com/problems/course-schedule/description/

from typing import List


# O(v + e) time | O(v) space, v --> number of courses
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for index, prereq in prerequisites:
            graph[index].append(prereq)
        stage = [0] * numCourses

        def dfs(index):
            if stage[index]:
                return True
            stage[index] = 1
            for prereq in graph[index]:
                if stage[prereq] == 1 or not dfs(prereq):
                    return False
            stage[index] = 2
            return True

        for index in range(len(graph)):
            if not dfs(index):
                return False
        return True
