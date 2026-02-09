"""
Pretty easy - just calculate current area by using the min of the two heights of your two pointers and the difference in indexes (horizontal length). Then, possibly overwrite the overall maxArea
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            computedArea = min(heights[l], heights[r]) * (r - l)
            maxArea = max(computedArea, maxArea)
            # adjust either the left or right pointer
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxArea
