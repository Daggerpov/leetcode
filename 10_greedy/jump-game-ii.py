"""
Creating a sliding window of sorts to keep track of a sliding window, of which indexes
can be jumped to within every level of jumps. to begin with, the only index that can
take 0 jumps is the first, then any indexes it can jump to become jumpable within 1
jump. We update l and r pointers to adjust for this minimum next level of BFS and
maximal (furthest jump). Then, returning the jump level from BFS iterating
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        res = 0

        while r < len(nums) - 1:
            farthestPointJumpable = 0
            for i in range(l, r + 1): # + 1 for inclusivity
                farthestPointJumpable = max(farthestPointJumpable, i + nums[i])
            
            # shifting our current jumping BFS level/window
            l = r + 1
            r = farthestPointJumpable 
            res += 1

        return res
