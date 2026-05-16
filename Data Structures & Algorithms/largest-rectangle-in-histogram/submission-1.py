class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mm=0
        for i in range(len(heights)):
            m=heights[i]
            l=i-1
            r=i+1
            c=1
            while l>=0 or r<=len(heights)-1:
                if l>=0 and heights[l]>=heights[i]:
                    c+=1
                    l-=1
                elif r<=len(heights)-1 and heights[r]>=heights[i]:
                    c+=1
                    r+=1
                else:
                    break
            m=heights[i]*c
            print(heights[i],c)
            mm=max(m,mm)
            c=1
        return mm