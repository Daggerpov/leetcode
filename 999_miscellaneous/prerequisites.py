# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array

# [0, 1], [0, 2]

# [0, 1], [1, 0] -> valid input?

# empty inputs -> []?

# n = 5, prereqs = [] -> any order.

# n = 0, prereqs = [5, 2] -> []
# n = 5, prereqs = [7, 2] -> doesn't exist

# adj = {course: [prereqs]}

# DFS + cycle check -> O(E * V)

# Topological sort: pop back->front courses that can be taken, removing 
# prereq pointers onto them (indegree)

# indegree == 0 (can take it freely)

# indegree = n (n many courses before it)

# build adj list -> set indegrees of each course by traversing adj list (check cycles -> return [])

# perform topological sort: popping from this queue -> check if indegree == 0

# visit the neighbours (courses that depend on this one)

# as popped, append this to res (course ordering)

from collections import defaultdict

class Solution:
    # numCourses = 5, prerequisites = [2, 3], [4, 1], [2, 1], [4, 0] 
    # expect: 0, 1, 3, 2, 4

    # numCourses = 2, prerequisites = [0, 1]
    # Time: O(E + V), Memory: O(E + V)
    def findOrder(self, numCourses: int, prerequisites):
        # build adj list
        # O(E * V), for E = prerequisites, V = numCourses

        # memory: O (E)
        adj = defaultdict(list)
        # Time: O(E)
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        # adj[0] = [], adj[1] = [], adj[2] = [3, 1], adj[3] = [], adj[4] = [1, 0]

        coursesTaken = {i: False for i in range(numCourses)} # courseNum: taken (True/False)
        # coursesTaken = {0: True, 1: True, 2: True, 3: True, 4: False ... False}
        visiting = set() # to avoid cycles, = (0, 1, 2, 3)
        res = [] # = [0, 1, 3, 2, 4]

        # False = cycle, True = not cycle
        # 0, 1, 2, 3
        # O(V + E), for E = prerequisites, N = numCourses
        def dfs(numCourse):
            # cycle check based on visiting 
            if coursesTaken[numCourse]:
                return True
            if numCourse in visiting:
                return False
            
            visiting.add(numCourse)
            
            # [3, 1]
            # O(E)
            for prereq in adj[numCourse]:
                # haven't taken it
                if coursesTaken[prereq] == False:
                    # 3
                    if not dfs(prereq):
                        return False

            # visit neighbours
            coursesTaken[numCourse] = True
            res.append(numCourse)
            visiting.remove(numCourse)
            return True
        
        # O(V)
        for i in range(numCourses): # 0, n -1
            if not dfs(i):
                return []
        
        return res 

soln = Solution()
print(soln.findOrder(numCourses = 5, prerequisites = [[2, 3], [4, 1], [2, 1], [4, 0]]))


import heapq as hq
nums=[1234]
hq.heapify(nums)
