'''
75. Sort Colors
Medium
Topics
premium lock icon
Companies
Hint
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

l = 0
r = len(nums) - 1

if 0: swap with l + incr l
if 1: middle 
if 2: swap with r + decr r
l, i, r = 0, 0, len(nums) - 1

if 0: swap with l + incr l
if 1: skip + i += 1
if 2: swap with r + decr r

if nums[i] == 2: i -= 1

time: O(n) memory: O(1)

1. interview structure 4/5
2. algorithm knowledge 3/5
3. python knowledge 3.5/5
4. debugging 5/5

[0,0,1,1,2,2]

Input: nums = [0,1,1,1,2,2] [0, 0, 1, 1, 1, 1, 2, 2]
                 l   r
                       i
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

'''
from typing import List
def sort_colours(nums: List[int]):
    l, i, r = 0, 0, len(nums) - 1
    # l = 0, i = 0, r = 5
    
    # nums = [0,1,1,2,0,2]
    #         l        r
    #           i
    while i < r + 1:
        if nums[i] == 0:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
        elif nums[i] == 2:
            nums[r], nums[i] = nums[i], nums[r]
            r -= 1
            if nums[i] == 0: continue
        
        if nums[i] != 2: i += 1

print(sort_colours([1, 0, 2]))


print(sort_colours([2, 0, 1, 2, 2, 1, 0, 0, 1]))
    
