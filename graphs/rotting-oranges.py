"""
BFS:
Initially, go through all cells and increment fresh for every fresh and append rotten
cell (r, c) tuples to q.
Increment minutes at each level of q. For each neighbour (4 directional), if it's in
bounds and a fresh fruit, rot it and append to q for next level BFS. Decrement num
fresh fruits.
Finally, if fresh == 0, then it was possible to rot every single one in minutes,
otherwise return -1
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        # normally, for BFS, we just do while q:
        while fresh > 0 and q:
            # rotten
            for i in range(len(q)):
                r, c = q.popleft()

                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        # rot a fresh fruit
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        # if fresh != 0 -> we didn't rot all fresh fruit
        return time if fresh == 0 else -1
