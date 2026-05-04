class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        c=0
        maxl,maxr=height[0],height[-1]
        l,r=0,len(height)-1
        while l<r:
            if maxl<maxr:
                l+=1
                maxl=max(maxl,height[l])
                c+=maxl-height[l]
            else:
                r-=1
                maxr=max(maxr,height[r])
                c+=maxr-height[r]
        return c