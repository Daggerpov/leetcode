"""
If not sorted (regular): Iterate through array (enumerate, to get indexes), storing each num in a hashmap (num: index), then if you calculate the current needed num, target - num to be in the hashmap, return their indexes.

If sorted: could use two pointers, such that if the sum is too large, move right pointer in, and if the sum is too small, move the left pointer in. If the pointers cross -> return False
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {} # {number: index} #hashmap

        for index, number in enumerate(nums):
            number_needed = target - number
            if number_needed in dictionary:
                return [dictionary[number_needed], index]
            # essentially else to that condition ^^ above

            if number not in dictionary:
                dictionary[number] = index
            # if number is in dictionary already, then nothing needs to be done
