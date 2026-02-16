class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # + 1 to account for the edges of the grid
        dp = [0] * (len(t) + 1)
        nextDp = [0] * (len(t) + 1)

        # to avoid N * M space -> just store cur and next row
        dp[len(t)] = nextDp[len(t)] = 1
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                nextDp[j] = dp[j]
                if s[i] == t[j]:
                    nextDp[j] += dp[j + 1]
            dp = nextDp[:]

        return dp[0] # top left
