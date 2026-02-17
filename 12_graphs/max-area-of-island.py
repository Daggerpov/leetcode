"""
Same thing as in Number of Islands, but with every valid land piece part of that island,
increment its DFS call's curIslandSize and return it all, with its sub-calls'
curIslandSize vars added up:

curIslandSize = 1 + dfs(curRow + 1, curCol) + \
dfs(curRow, curCol + 1) + \
dfs(curRow - 1, curCol) + \
dfs(curRow, curCol - 1)

return curIslandSize
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        if not grid: return None

        visited = set()

        # run DFS from every 1 cell

        # mark 1s as visited

        # on subsequent runs, if a cell is already visited, skip,
        # not increasing the number of islands, `res`

        # returns True if traversing new island
        def dfs(row, col):
            if row in [-1, len(grid)] or col in [-1, len(grid[0])] or grid[row][col] == 0 or (row, col) in visited:
                # out of bounds or already visited
                return 0
            
            visited.add((row, col))

            area = 1

            # traverse in all directions, marking the 1s as visited
            deltaDirections = [[0, 1], [0, -1], [-1, 0], [1, 0]]

            for deltaRow, deltaCol in deltaDirections:
                area += dfs(row + deltaRow, col + deltaCol)
            
            return area

        for row in range(len(grid)): # rows
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    res = max(res, dfs(row, col))

        return res
