class Solution:
    def numDecodings(self, s: str) -> int:
        # only need these 3 vars of the array, since we only access
        # dp[i], dp[i + 1], dp[i + 2]
        dp = dp2 = 0 # dp = dp[i], dp2 = dp[i + 2]
        dp1 = 1 # dp1 = dp[i + 1]

        # (bottom-up dp)
        for i in range(len(s) - 1, -1, -1):
            # can't decode
            if s[i] == "0":
                dp = 0
            else:
                # decode as current num 1-digit
                dp = dp1

            # valid 2-digit num (10-26)
            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"
            ):
                # skip to 2 indexes ahead (since we consider s[i] and s[i+ 1] as 2-digit)
                dp += dp2
            dp, dp1, dp2 = 0, dp, dp1
        return dp1
