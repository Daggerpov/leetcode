"""
Calculate the prefix sums in order, with prefix = 1 to start. Then, calculate the postfix sums in order, with postfix = 1 to start (by iterating in reverse using for i in range(len(nums) - 1, -1, -1): . As going through each list, multiply the pre/postfix with the res[i] : res[i] *= postfix
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix, postfix = 1, 1

        # [1, 1, 1, 1]
        
        for index, num in enumerate(nums):
            res[index] *= prefix
            prefix *= num
            
        for index in range(len(nums) - 1, -1, -1):
            res[index] *= postfix
            postfix *= nums[index]
        
        return res
