class Solution:
    # nums = [] -> 0, [1] -> 1, [2, 3] -> 2, [4, 5, 8] -> 2
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0

        for i in range(len(nums)): # 0 -> len(nums) - 1, therefore, the indexes
            if nums[i] - 1 in hashSet:
                # nums[i] isn't the first in its sequence, therefore skip
                continue
            # now we know it has the potential of being the subsequence start
            current_length = 1
            while nums[i] + current_length in hashSet:
                current_length += 1
            
            longest = max(longest, current_length)
        return longest
