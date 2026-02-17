"""
Iterate through the array (street), finding max(rob1 + n, rob2) (since they'd be
ordered rob1, rob2, n, and you can rob either both of the ends or the middle) -> then,
just update the rob1 and rob2 pointers rightward as you traverse. What you find with
the max through each iteration could be the global max of the array/street.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for i in nums:
            cur = max(i + rob1, rob2) # since we can't take adj houses
            rob1 = rob2
            rob2 = cur
        
        return rob2 # last cur
