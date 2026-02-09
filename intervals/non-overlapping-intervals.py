class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])
        res = 0

        prevEnd = intervals[0][1] # can reliably do this since intervals.length >= 1

        for start, end in intervals[1:]:
            # overlapping
            if start < prevEnd:
                res += 1
                prevEnd = min(end, prevEnd)
            else:
                prevEnd = end
        
        return res
