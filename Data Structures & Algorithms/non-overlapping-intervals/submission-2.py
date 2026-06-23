class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        stack = [intervals[0]]

        for j in range(1, len(intervals)):
            if stack[-1][1] <= intervals[j][0]:
                stack.append(intervals[j])
            else:
                if intervals[j][1] < stack[-1][1]:
                    stack.pop()
                    stack.append(intervals[j])

        return len(intervals) - len(stack)