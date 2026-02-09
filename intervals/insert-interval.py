class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # loop through intervals by start
        # check for when start of that interval > newInterval's start

        # -> need to insert `newInterval` before that one
        
        res = []

        for i in range(len(intervals)):
            # if the new interval's end is less than the cur
            # interval's start

            # a.k.a. if the cur interval's start is greater than 
            # the new interval's end
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # if the cur interval's end is less than 
            # the new interval's start
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # overlap, so merge
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res
