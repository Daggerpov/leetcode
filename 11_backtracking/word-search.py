class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])
        def dfs(curRow, curCol, targetIndex):
            if curRow not in range(height) or curCol not in range(width):
                return False
            char = board[curRow][curCol]
            if char != word[targetIndex]:
                return False
            if targetIndex == len(word) - 1:
                # finished compelting word
                return True

            temp = char
            board[curRow][curCol] = "#"

            if dfs(curRow + 1, curCol, targetIndex + 1) or\
            dfs(curRow - 1, curCol, targetIndex + 1) or\
            dfs(curRow, curCol + 1, targetIndex + 1) or\
            dfs(curRow, curCol - 1, targetIndex + 1):
                return True
            
            board[curRow][curCol] = temp
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True

        return False
