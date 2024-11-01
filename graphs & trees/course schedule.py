""" You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.

Example 1:

Input: numCourses = 2, prerequisites = [[0,1]]

Output: true
Explanation: First take course 1 (no prerequisites) and then take course 0.

Example 2:

Input: numCourses = 2, prerequisites = [[0,1],[1,0]]

Output: false
Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.

Constraints:

1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
All prerequisite pairs are unique. """


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {course:[] for course in range(numCourses)}
        for course, prereq in prerequisites:
            preReq[course].append(prereq)
        visitedCourses = set()
        def dfs(course):
            if course in visitedCourses:
                return False
            if preReq[course] == []:
                return True
            visitedCourses.add(course)
            for precourse in preReq[course]:
                if not dfs(precourse):
                    return False
            visitedCourses.remove(course)
            preReq[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            
        