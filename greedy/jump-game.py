def canJump(self, nums: List[int]) -> bool:

    # greedy solution:
    # - start from the last index
    # -> see which previous indexes can take me there
    # - keep decreasing the subproblem until I 
    
    # - either reach the first index -> return True
    # - or only surpass it -> return False
    
    startPoint = len(nums) - 1 # initially last index
    
    # iterate backwards -> starting at 2nd last index
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] + i >= startPoint:
            startPoint = i
        # otherwise, check if there's a further back 
        # index that has a jump great enough to 
        # get to the current `startPoint`
    
    return startPoint <= 0
