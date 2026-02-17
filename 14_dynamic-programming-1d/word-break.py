class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # marking all words as false by default
        dp[len(s)] = True # reached end

        # bottom-up DP going from back of string, 
        # trying to chip away words (similar to coin change)
        for i in range(len(s) - 1, -1, -1):
            # similar to for c in coins in coin change
            for w in wordDict:
                # can take this word (2nd operand), within bounds (1st operand)
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    # try out possibility of taking this word (coin)
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    # a valid word that takes to end
                    # so, don't try other words
                    break

        # if we could reach end from start
        return dp[0]
