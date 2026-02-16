
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]


        # memoized:
        '''
        if len(s1) + len(s2) != len(s3):
            # invalid case
            return False

        # need to loop through s3, then at every point, 
        # see if it's the current interleaving of s1 & s2

        # bottom up means going from both full strings at the end

        memo = {}

        def dfs(i1, i2):
            if (i1, i2) in memo:
                return memo[(i1, i2)]
            # done
            if i1 + i2 == len(s3): 
                return True
            
            # continue pursuing the correct track
            if i1 < len(s1) and s3[i1 + i2] == s1[i1]:
                if dfs(i1 + 1, i2): 
                    memo[(i1 + 1, i2)] = True
                    return True

            if i2 < len(s2) and s3[i1 + i2] == s2[i2]:
                if dfs(i1, i2 + 1): 
                    memo[(i1, i2+1)] = True
                    return True

            memo[(i1, i2)] = False
            return False

        return dfs(0, 0)
        '''
