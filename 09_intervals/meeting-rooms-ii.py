"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        maxNum, curNumRooms = 0, 0

        s, e = 0, 0

        while s in range(len(starts)):
            if starts[s] < ends[e]:
                # start a meeting (require one more room)
                s += 1
                curNumRooms += 1
            else: # ends[e] <= starts[s]
                # end a meeting (require one less room)
                e += 1
                curNumRooms -= 1
            maxNum = max(maxNum, curNumRooms)
        
        return maxNum
