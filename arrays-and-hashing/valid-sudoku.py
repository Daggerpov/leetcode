"""
Set columns, rows, and squares = collections.defaultdict(set) . Loop through every cell, adding to those sets if it's not already in any, current Val in columns[r] or currentVal in rows[c] or currentVal in squares[(r//3, c//3)]  -> return False if it's already in any of these (duplicate, by Sudoku rules).
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                currentVal = board[r][c]
                if currentVal == ".":
                    continue
                if currentVal in columns[r] or currentVal in rows[c] or currentVal in squares[(r//3, c//3)]:
                    return False
                else:
                    # need to put in columns, rows, squares
                    columns[r].add(currentVal)
                    rows[c].add(currentVal)
                    squares[(r//3, c//3)].add(currentVal)
        return True
