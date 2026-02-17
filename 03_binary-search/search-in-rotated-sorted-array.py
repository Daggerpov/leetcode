class Solution:
    def search(self, nums: List[int], target: int) -> int:
        target_index = -1

        # run binary search

        # examples are from example input/output #1
        
        # if target (e.g. 1) < computed middle (e.g. 5) is:
        # if we're in the left portion: 
        # - we search to the left of the computed middle 
        # - we eliminate what's to the right of the computed middle, in the left portion
        # otherwise, we're in the right portion: 
        # - we search to the left of the computed middle 
        # - we eliminate what's to the right of the computed middle, in the right portion

        # if target > computed middle is:
        # if we're in the left portion: we search to the right of the computed middle
        # if we're in the right portion: 

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2 
            midNum = nums[mid]
            # l + ((l+r) // 2) # check later

            if target == midNum:
                return mid
            
            # we're in the left portion
            if nums[l] <= midNum:
                if target > midNum or target < nums[l]:
                    # we need to search within the right portion
                    l = mid + 1
                else:
                    # search in this left portion
                    r = mid - 1
            # we're in the right portion
            else:
                if target < midNum or target > nums[r]:
                    # we need to search within the left portion
                    r = mid - 1
                elif target > midNum:
                    # search in this left portion
                    l = mid + 1

        return target_index
