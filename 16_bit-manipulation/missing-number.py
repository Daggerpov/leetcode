class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        for i in range(n):
            # i is what's supposed to be there
            # nums[i] is what's actually there
            xorr ^= i ^ nums[i] 
            
        # here, we know that what's left is 
        # a num that was formerly i in the loop
        # but wasn't nums[i] (actually there)
        return xorr
