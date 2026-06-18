class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z=[101,0,0],[0,101,0],[0,0,101]
        def find(p,l):
            l[0]=max(p[0],l[0])
            l[1]=max(p[1],l[1])
            l[2]=max(p[2],l[2])
            return l
        for i in triplets:
            if i[0]==target[0]:
                x=i
            if i[1]==target[1]:
                y=i
            if i[2]==target[2]:
                z=i
            if x[0]!=101 and y[1]!=101 and z[2]!=101:
                y=find(x,y)
                z=find(y,z)
                if z==target:
                    return True
        return False