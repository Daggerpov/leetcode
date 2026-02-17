"""
Loop through, adding to hashset, but if num if already in hashset -> duplicate exists
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set();

        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False
