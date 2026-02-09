"""
(check whole code from the NeetCode problem)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)] # + 1, because I need 0 to len(nums)
        # [1, 4, 2, 2, 5, 5]
        # [[1, 4], [2, 5]], since indexes in this freq list rep nums that occurred that num times

        counts = defaultdict(int) # e.g. {3: 2}, means the number 3 has 2 occurrences

        for number in nums:
            counts[number] += 1
            # could've also used counts[number] = 1 + counts.get(number, 0)
        
        for number, count in counts.items(): # e.g. {1: 2, 2: 4, 3: 3}
            freq[count].append(number) # freq = [[], [], [1], [3], [2]]

        # freq = [[], [], [1], [3], [2]]

        top_elements = []

        # i is iterating from last index to first
        for i in range(len(freq) -1, -1, -1):
            for element in freq[i]:
                top_elements.append(element)
                if len(top_elements) >= k:
                    # stop
                    return top_elements

        return top_elements
