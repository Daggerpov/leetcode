class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            median = (l + r) // 2
            if nums[median] > target:
                r = median - 1
            elif nums[median] < target:
                l = median + 1
            else:
                return median
            
        return -1
