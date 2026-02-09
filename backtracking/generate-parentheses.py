class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openCount, closedCount, curString):
            if openCount == n == closedCount:
                # done
                res.append(curString)
            if closedCount < openCount:
                # could add closed, since we can only close open ones
                backtrack(openCount, closedCount + 1, curString + ")")
            if openCount < n:
                # could add opened
                backtrack(openCount + 1, closedCount, curString + "(")

        backtrack(0, 0, "")
        return res
