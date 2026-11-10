class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x=nums1+nums2
        x=sorted(x)
        if len(x)%2==0:
            a=(len(x)//2)-1
            b=a+1
            return (x[a]+x[b])/2
        else:
            return x[len(x)//2]