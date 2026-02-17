from collections import defaultdict
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int) # {sum: ways to form sum}
        
        dp[0] = 1

        for num in nums:
            nextDP = defaultdict(int)

            for sum, ways in dp.items():
                minus_res = sum - num
                plus_res = sum + num
                nextDP[minus_res] += ways
                nextDP[plus_res] += ways

            dp = nextDP
        
        # should eventually end up with dp = all sums, so this will be the solution
        return dp[target]

