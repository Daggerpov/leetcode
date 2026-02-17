"""
DFS:

run DFS on all connected nodes (by using directions array and for loop)

- have to bounds check any time directions are used
- If it's 0, water, then it's not part of the island -> return False
- If it's already in visited (of type set()), then it's not a different island -> return False
    - Otherwise, add it to visited
- Otherwise, return True at the end of this DFS search, since it's a whole island
    - After running DFS on all land cells in graph, increase islandCount if DFS returned True (it is an island, with lands that haven't previously been visited
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if not grid: return None

        visited = set()

        # run DFS from every 1 cell

        # mark 1s as visited

        # on subsequent runs, if a cell is already visited, skip,
        # not increasing the number of islands, `res`

        # returns True if traversing new island
        def dfs(row, col):
            if row in [-1, len(grid)] or col in [-1, len(grid[0])] \
                or grid[row][col] == "0" or (row, col) in visited:
                # out of bounds or already visited
                return False
            
            visited.add((row, col))

            # traverse in all directions, marking the 1s as visited
            deltaDirections = [[0, 1], [0, -1], [-1, 0], [1, 0]]

            for deltaRow, deltaCol in deltaDirections:
                newRow, newCol = row + deltaRow, col + deltaCol
                dfs(newRow, newCol)
            
            return True

        for row in range(len(grid)): # rows
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    if dfs(row, col): res += 1

        return res
