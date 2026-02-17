"""
- Keep checking if curSum is the new maximal sum, res
- if curSum drops below 0, reset it
- Return maximal sum res

(Kadane's Algorithm)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curSum = 0

        for num in nums:
            curSum += num
            res = max(res, curSum)
            # reset
            if curSum < 0:
                curSum = 0

        return res
