"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        i = sorted(intervals, key=lambda x: x.start)
        for j in range(1,len(i)):
            if i[j-1].end<=i[j].start:
                continue
            elif i[j-1].start>=i[j].end:
                continue
            else:
                return False
        return True