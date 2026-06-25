class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # sort by end time
        # keep interval with the earlier end time so future intervals have more time 
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                count += 1
            else:
                prev_end = end

        return count