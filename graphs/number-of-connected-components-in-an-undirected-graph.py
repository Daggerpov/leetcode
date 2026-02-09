"""
Union Find:
Write a find algorithm, which simply looks up the parent over and over of the node. Can
add par[res] = par[par[res]] for optimization. Then, as unions are done successfully,
decrease overall res, since a connection reduces the # connected components.

DFS (worse):

Create adjacency list

adj = {i: [] for i in range(n)}
for i, j in edges:
    adj[i].append(j)
    adj[j].append(i)

DFS for all node and its edges (neighbors). Every time this is done, increase
components count
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ## THE UNION FIND SOLUTION:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            # shouldn't directly operate on node
            res = node

            # until we can't traverse up higher (both same)
            while res != par[res]:
                # keep traversing both the rest and parent up
                par[res] = par[par[res]]
                res = par[res]

            return res
        
        def union(n1, n2):
            # find up-most grandparents
            p1, p2 = find(n1), find(n2)

            # if they're already unified
            if p1 == p2:
                return 0

            # union p1 into p2
            if rank[p2] > rank[p1]:
                # set p1's parent to p2 (union)
                par[p1] = p2
                # increase p2's rank
                rank[p2] += rank[p1]
            # opposite case:
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
