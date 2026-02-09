class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        minVal = float("inf")

        while l <= r:
            mid = (l+r) // 2 
            midNum = nums[mid]
            minVal = min(minVal, midNum)
            # we're in the left portion
            if nums[r] < midNum:
                # search the right portion
                l = mid + 1
            # we're in the right portion
            else:
                # search to the left, since all values
                # to the right, within this right portion
                # are going to be greater than midNum
                r = mid - 1

        return minVal
