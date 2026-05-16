class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea=0
        stack=[] #pair        
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                maxarea=max(maxarea,height*(i-index))
                start=index
            stack.append([start,h])
        for i in stack:
            maxarea=max(maxarea,i[1]*(len(heights)-i[0]))
        return maxarea
