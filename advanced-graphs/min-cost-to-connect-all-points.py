"""
Adjacency lists, with manhattan distances computed

Prim's Algorithm:
- Pick a node
- Calculate distances of neighbours
- Add neighbours to minheap, even if duplicate, unless visited already
"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # {point_index: [(dist1, idx1), (dist2, idx2)]}
        adj = { point: [] for point in range(len(points)) } 

        # build adjacency lists
        for idx1, num1 in enumerate(points):
            x1, y1 = num1
            for idx2, num2 in enumerate(points):
                x2, y2 = num2

                distance = abs(x2 - x1) + abs(y2 - y1)

                adj[idx1].append((distance, idx2))
                adj[idx1].append((distance, idx1))

        # Prim's algorithm

        # initialize minheap with distances of 0
        minHeap = [[0, 0]] # 0 = first point

        visited = set()
        res = 0

        # TODO: possibly add check if disconnected components in graph
        while len(visited) < len(points):
            cost, pointIdx = heapq.heappop(minHeap)
            if pointIdx in visited:
                continue # skip this one
            visited.add(pointIdx)
            res += cost

            for neighbour in adj[pointIdx]:
                cost, idx = neighbour
                if idx not in visited:
                    heapq.heappush(minHeap, (cost, idx))

        return res
