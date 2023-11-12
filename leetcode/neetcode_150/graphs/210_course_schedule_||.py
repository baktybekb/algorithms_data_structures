from typing import List


# O(v + e) time | O(v) space, v --> number of courses
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for index, prereq in prerequisites:
            graph[index].append(prereq)
        stage, order = [0] * numCourses, []

        def dfs(index):
            if stage[index] == 2:
                return True
            stage[index] = 1
            for prereq in graph[index]:
                if stage[prereq] == 1 or not dfs(prereq):
                    return False
            stage[index] = 2
            order.append(index)
            return True

        for index in range(len(graph)):
            if not dfs(index):
                return []
        return order
