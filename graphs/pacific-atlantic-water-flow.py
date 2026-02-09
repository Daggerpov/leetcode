"""
Call dfs on all edge cells, passing in by reference the set() for either pacific or
atlantic. At the end, I'll append to res the overlapping good cells from pacific and
atlantic. While in DFS, if out of bounds, already in the visited set (pacific or
atlantic), or its own height is less than previous (inverted conditional since going
from edge inward), return False. Else, add to visited and call recursively in all
4 directions.
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # As the traversal is happening, mark all cells where the 
        # height is greater than the calling cell (the previous one)
        # -> therefore, it can be reached from this edge

        # Do this for pacific ones, then as this is being done 
        # for atlantic ones, I can check if it's valid for atlantic AND
        # pacific -> therefore, put that into the results list

        res = []

        pacific, atlantic = set(), set()
        ROWS, COLS = len(heights), len(heights[0]) 

        def dfs(curRow, curCol, visited, prevHeight):
            # bounds check or if cur cell couldn't have been reached, since it's less than prevHeight
            if (curRow, curCol) in visited or curRow in [-1, ROWS] or curCol in [-1, COLS] or heights[curRow][curCol] < prevHeight:
                return False
            
            visited.add((curRow, curCol))

            # set the current height val, to pass into dfs for next prevHeight
            curVal = heights[curRow][curCol]

            # Run recursively in all 4 directions
            for i in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                dfs(curRow + i[0], curCol + i[1], visited, curVal)

        for c in range(COLS):
            # for every column in row 0 (top edge)
            dfs(0, c, pacific, heights[0][c])
            # for every column in last row (bottom edge)
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        for r in range(len(heights)):
            # for every row in col 0 (left edge)
            dfs(r, 0, pacific, heights[r][0])
            # for every row in last col (right edge)
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                # append overlapping cells that were reached
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res

# Alternative solution:

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))

        pacific = []
        atlantic = []
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res
