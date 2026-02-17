from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            # since we're tracking the row, we know that we won't place
            # two queens on the same row. So, we only need to worry about 
            # queens attacking each other on columns.
            if r == n:
                # solution; hit n queens
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                # can attack in col, positive diagonal, or negative diagonal.
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # if we do put the queen there
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                # if we don't put the queen there
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
