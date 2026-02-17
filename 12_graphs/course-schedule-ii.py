"""
Same as Course Schedule, but maintain visited as a whole, to avoid doing same course
twice. Once course and its pre-reqs have been traversed, add to visited and append to
overall res. Again, like with Course Schedule, if ever there's a cycle detected
(i.e. if crs in visiting:), then return [] since there's no valid course ordering
to traverse.
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting = set()
        visited = set()

        res = [] #ordering of prerequisites to take

        # construct an adjacency list of each course: prerequisites

        adj = {crs: [] for crs in range(numCourses)}

        for crs, prereq in prerequisites:
            adj[crs].append(prereq)

        def dfs(crs):
            if crs in visiting:
                # cycle detected
                return False
            if crs in visited:
                # we've already taken it
                return True
            
            visiting.add(crs)
            
            for prereq in adj[crs]:
                # try to take those courses
                if not dfs(prereq): return False # cycle detected
            
            visiting.remove(crs)
            visited.add(crs)
            
            # take a course
            res.append(crs)
            return True
            
        for crs in range(numCourses):
            if not dfs(crs): return [] # cycle detected

        return res
