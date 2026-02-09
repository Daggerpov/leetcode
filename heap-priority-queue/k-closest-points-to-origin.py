"""
Calculate the distance from the point to the origin, storing in distances = [] by appending ((x**2 + y**2), x, y), then heapq.heapify(distances) - it will heapify based on the first element within each distance, x**2 + y**2. Aterwards, while distances and k > 0: , heapq.heappop(distances) to get the min distance (all heaps in Python are min by default) - add that to the resulting distances which will be returned.
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distances.append([(x**2) + (y**2), x, y])
        
        # by default, Python uses a minHeap
        heapq.heapify(distances) # will store all values in minHeap
        res = []

        while distances and k > 0: # check if more results are needed
            # add closest point (minimum distance) to result
            distance, x, y = heapq.heappop(distances)
            res.append([x, y])
            k -= 1

        return res
