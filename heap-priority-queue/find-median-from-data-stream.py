class MedianFinder:
    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        
        # large is a min heap, small is a max heap (using negatives in Python)
        self.small, self.large = [], []  

    def addNum(self, num: int) -> None:
        # if num if larger than large's smallest
        # -> it belongs in large
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            # give small's biggest value to large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            # give large's biggest value to small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # odd-length, so take the middle-most element
        # which is the largest small or smallest large
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        # even-length, so take the average of the 
        # middle-most elems (largest small, smallest large)
        return (-1 * self.small[0] + self.large[0]) / 2.0
