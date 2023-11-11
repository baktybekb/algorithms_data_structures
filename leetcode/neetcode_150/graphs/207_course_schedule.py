# https://leetcode.com/problems/course-schedule/description/

from typing import List


# O(n) time | O(n) space, n --> number of courses
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course_id, prereq in prerequisites:
            graph[course_id].append(prereq)
        processed = [0] * numCourses  # 0 - not processed, 1 - in process, 2 - finished (can skip)
        for course_id in range(len(graph)):
            if not self.dfs(processed, graph, course_id):
                return False
        return True

    def dfs(self, processed, graph, course_id):
        processed[course_id] = 1
        for prereq in graph[course_id]:
            if processed[prereq] == 2:
                continue
            if processed[prereq] == 1 or not self.dfs(processed, graph, prereq):
                return False
        processed[course_id] = 2
        return True
