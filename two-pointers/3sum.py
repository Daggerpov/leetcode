"""
Sort first (n log n but that's fine). Then, iterate through, calling current num a, then search for b and c using two pointers, from current index (left) and end index (right) -> search inwards.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        
        for numIndex in range(len(nums)):
            # num is operand a, where a + b + c = 0
            a = nums[numIndex]
            
            #(current num is same as last) -> don't bother checking
            if numIndex > 0 and a == nums[numIndex - 1]: 
                continue

            # two-pointers to find the other two operands (b and c) for addition
            l, r = numIndex + 1, len(nums) - 1

            # they have not crossed
            # OG two-pointers twoSum
            while l < r:
                b, c = nums[l], nums[r]
                curSum = a + b + c

                # later: if different sums are targeted (desired), edit this:
                if curSum < 0:
                    l += 1
                elif curSum > 0:
                    r -= 1
                else:
                    # correct sum
                    res.append([a, b, c])
                    # need to move left pointer over to non-duplicate number
                    l += 1
                    # same conditional as before:
                    #(current num is same as last) -> don't bother checking
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # we've reached a new num
        return res
