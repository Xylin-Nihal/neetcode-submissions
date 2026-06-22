class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack=[]
        intervals=sorted(intervals)
        for i in intervals:
            if not stack:
                stack.append(i)
            if stack[-1][1]<i[0]:
                stack.append(i)
            elif stack[-1][0]>i[1]:
                x=stack.pop()
                stack.append(i)
                stack.append(x)
            else:
                k,l=min(stack[-1][0],i[0]),max(i[1],stack[-1][1])
                stack.pop()
                stack.append([k,l])
            
        return stack