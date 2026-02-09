"""
Put chests in queue

BFS on q, incrementing chestDistance after each full exhaustive loop of q, to use as value
replacing cur cell with (note: i often make the mistake of taking curCell = grid[r][c],
without remembering that curCell is just a value, not reference to grid[r][c]. So, maybe
just don't do this curCell = grid[r][c] line anywhere.
"""

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque() # will contain tuples of the chests' positions, at first
        # but once I start running BFS, it'll continue onto land cells

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    # mark the treasure chests
                    q.append((r, c))
            
        # run BFS from each chest at the same time

        # mark each land cell that can be traversed with its
        # distance from the nearest chest

        chestDistance = 0
        while q:
            # for each cell in this BFS "ring" (adjacent cells)
            for i in range(len(q)):
                curRow, curCol = q.popleft()

                if curRow in [-1, ROWS] or curCol in [-1, COLS] or (curRow, curCol) in visited or grid[curRow][curCol] == -1:
                    continue # skipping this direction traversal

                visited.add((curRow, curCol))
                
                grid[curRow][curCol] = chestDistance
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
                for dx, dy in directions:
                    q.append((curRow + dx, curCol + dy))

            chestDistance += 1
