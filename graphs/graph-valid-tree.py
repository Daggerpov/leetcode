"""
Two rules of valid trees: non-cyclical + all connected (no separated components)

Populate adjacency list with edges list:

for n1, n2 in edges:
    adj[n1].append(n2)
    adj[n2].append(n1)

Maintain visited set. If a node has already been visited, there's a cycle, and return False

Otherwise, add to visited and go through that node's adjacency list, returning false if
any recursive DFS calls returns False, except if j == prev (pass inner arg prev to keep
track of current node's parent, since that connection is OK for there to not be a cycle.

At the end, if all have been traversed fine after dfs(0, -1) (with 0 being index) and
n == len(visited) (meaning there aren't any separated components) -> return True
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # what is a valid tree?
        # 1. no cycles
        # 2. is all connected (i.e. no separate connected portions)

        if not n:
            return True
        adj = {i: [] for i in range(n)}
        # creating adjacency list for each pair of edges
        # this is done bidirectionally, since all of the edges are such
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set() # keep track of seen nodes
        # if we see a node (that isn't a node's direct parent, as we
        # check for later) that's already been seen before -> there's a cycle

        def dfs(i: int, prev: int) -> bool:
            # detect a cycle
            if i in visited:
                return False

            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    # ignore the previous node, since it doesn't indicate
                    # that there's a cycle, just because it's connected
                    # to its parent
                    continue
                if not dfs(j, i):
                    # returning false if the call was False (i.e. j, which 
                    # we pass in as i has been visiteded)
                    return False
            return True

        return dfs(0, float('inf')) and n == len(visited)
