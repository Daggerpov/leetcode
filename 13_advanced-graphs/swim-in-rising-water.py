from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]

        visited.add((0, 0))

        while minHeap:
            t, row, col = heapq.heappop(minHeap)
            
            # reached bottom right, so return time it took
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return t

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for deltaR, deltaC in directions:
                newRow, newCol = row + deltaR, col + deltaC
                if newRow in (-1, len(grid)) or newCol in (-1, len(grid[0])) or (newRow, newCol) in visited:
                    continue

                visited.add((newRow, newCol))
                heapq.heappush(minHeap, [max(t, grid[newRow][newCol]), newRow, newCol])

        return 0           
