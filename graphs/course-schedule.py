"""
Make an adjacency list, preMap = {i: [] for i in range(numCourses)}. Then, populate it
using the course <-> prerequisite edge list given.

Within DFS, check if cycle has occurred by if crs in visiting (False resulting output),
since course pre-req cycle means impossible (chicken vs. egg problem).

Add current course to visiting, visit its pre-reqs, then remove it from visiting.
Finally, set its preMap[crs] = [] and return True for this course. If any course ever
returns False, return False as a whole.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        # preMap = {i: [] for i in range(numCourses)}

        preMap = {}
        for i in range(numCourses):
            preMap[i] = []

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
