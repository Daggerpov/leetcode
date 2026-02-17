from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp goes from bottom-right to bottom-left, then up
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1): # coins backwards
            nextDP = [0] * (amount + 1) # [[0], [0], [0]]
            print(nextDP)
            nextDP[0] = 1

            for a in range(1, amount + 1): # [1, amount]
                nextDP[a] = dp[a]
                take_coin = a - coins[i]
                if take_coin >= 0:
                    nextDP[a] += nextDP[take_coin] # solution to taking a coin
            # after each row (bottom->up), we copy forth the 
            dp = nextDP

        # at this point, we have a 1D array of amounts solutions
        return dp[amount] # pick solution for this amount input
