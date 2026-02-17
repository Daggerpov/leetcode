"""
Same idea as with House Robber, but just getting the max of the two substrings: not
including the first and not including the last element of the array (street).

return max(nums[0], self.rob_sub_list(nums[1:]), self.rob_sub_list(nums[:-1]))
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for i in nums:
            cur = max(i + rob1, rob2) # since we can't take adj houses
            rob1 = rob2
            rob2 = cur
        
        return rob2 # last cur
