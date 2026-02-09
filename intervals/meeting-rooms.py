"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prevEnd = None
        intervals.sort(key=lambda i: i.start) # sort by start time
        for interval in intervals:
            start, end = interval.start, interval.end

            if prevEnd and prevEnd > start:
                return False
            prevEnd = end
            
        return True
