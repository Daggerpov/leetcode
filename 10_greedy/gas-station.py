"""
The greedy way to go about this is to assume that the first starting point that took us
to the end of the list will take us through the start of the list that we've 'skipped',
since we know that there's one unique solution and no prior ones got us to around
completely.
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1
        
        totalGasStorage = 0
        startingPoint = 0

        # profits = [-1, 0, -1, 3]

        # being greedy, we can assume that any starting point 
        # that took us from the `startingPoint` -> end of list
        # is the only unique solution that'll take us all the way

        for index in range(len(gas)):
            totalGasStorage += gas[index] - cost[index]
            if totalGasStorage < 0: 
                # wasn't a profitable starting point
                startingPoint = index + 1
                totalGasStorage = 0
        
        # if crossed over last index -> means we never found a good 
        # starting point that'll take us through the whole way
        return startingPoint if startingPoint <= len(gas) - 1 else -1
