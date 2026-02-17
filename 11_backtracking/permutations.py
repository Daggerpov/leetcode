class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        
        def getPermutations(curList, remaining):
            if not remaining:
                permutations.append(curList)
                return
            
            # put remaining into hashset to remove from
            remainingOptions = set(remaining)
            
            # this will generate all choices stemming from 
            # the curList, with every possible remaining value

            # this will then re-do that recursively until no remaining
            for remainingNum in remaining:
                # call getPermutations by choosing this num
                newList = curList + [remainingNum]
                remainingOptions.remove(remainingNum)
                getPermutations(newList, remainingOptions)
                remainingOptions.add(remainingNum)

        getPermutations([], nums) # base case: one number
        return permutations
