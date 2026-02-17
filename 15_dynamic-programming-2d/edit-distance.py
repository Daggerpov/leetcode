class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1
        # ensuring word 1 is smaller, since 
        # we'll be iterating over word 2 (n) more often

        # n + 1 to have the col out of bounds for continuity
        dp = [0] * (n + 1)
        nextDp = [0] * (n + 1)

        for j in range(n + 1):
            # the remaining characters needed to fill word 1
            # with chars in word 2 (n)
            dp[j] = n - j

        # bottom-up (with left axis being word1, m)
        for i in range(m - 1, -1, -1):
            # same as what we did before, with remaining swaps
            # the further down we are (closer to m being built),
            # the further we are from it being word 2, n

            # initialize the right-most char to this
            nextDp[n] = m - i
            # right-left (with top axis being word2, n)
            for j in range(n - 1, -1, -1):
                # if same char, needed 1 less change, since
                # we don't have to do this char
                if word1[i] == word2[j]:
                    nextDp[j] = dp[j + 1]
                else:
                    # min swaps out of: cur, next right one, cur right one

                    # going down a row, since we now need to find the 
                    # match for char i in m, but not char j in n
                    delete = dp[j] # (i, j+1)

                    # -> we increase this pointer since word 2's j now
                    # needs to find a match
                    insert = nextDp[j + 1] # (i + 1, j) 

                    # we now skip to the next char of each word
                    # which means going down a row (using dp instead of nextDP) 
                    # and over a column (j + 1)
                    replace = dp[j + 1] # (i + 1, j + 1)

                    # find best operation and use it
                    nextDp[j] = 1 + min(delete, insert, replace)
            dp = nextDp[:]

        # this will be top-left, soln
        return dp[0]
