"""
The question states it wants O(1) space, and we can do this by avoiding the hashmap as in Two Sum I, since we can leverage the fact that the input is sorted to use two pointers instead.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        # while they don't cross
        while left < right: 
            current_sum = numbers[left] + numbers[right] 
            if current_sum == target:
                return [left + 1, right + 1] # due to 1-indexing, per question
            else:
                # not hit target
                if current_sum > target:
                    # too big of sum, therefore we need to decrease it by moving right pointer left 
                    right -= 1
                else:
                    # too small of sum, therefore we need to increase it by moving left pointer right
                    left += 1
        
        # don't need to handle case where no solution exists
