"""
See the code
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones] #negative to behave as max heap
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -1 * heapq.heappop(stones) # -6
            second = -1 * heapq.heappop(stones) # -4
            if first > second:
                heapq.heappush(stones, -1 * (first - second))

        return -stones[0] if stones else 0
