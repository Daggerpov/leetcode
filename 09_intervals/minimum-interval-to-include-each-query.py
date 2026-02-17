class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda i: i[0])
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            # essentially iterating through intervals with i

            # and as long as the current interval's start is <= q,
            # so q could be in that interval
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                # pushing a tuple of the length of the interval, 
                # along with the end time, r
                heapq.heappush(minHeap, (end - start + 1, end))
                i += 1
            
            # popping from the minheap so long as there are elements
            # and those elements are invalid; can't be a suitable interval
            # to house q, because I've previously checked start times
            # but this validates the end time
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            # the result of this query is the shortest length interval
            # added by the first while loop (validating starts)
            # and was validated by the last while loop (validating ends)
            res[q] = minHeap[0][0] if minHeap else -1 # couldn't be found
        return [res[q] for q in queries]
