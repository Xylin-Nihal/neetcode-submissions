class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        h={}
        n=len(grid)
        r=[0,0]
        for i in range(len(grid)):
            for j in range(len(grid)):
                x=grid[i][j]
                if x in h:
                    h[x]+=1
                else:
                    h[x]=1
                
        print(h)
        for i in range(1,(n*n)+1):
            if i not in h:
                r[1]=i
            elif h[i]==2:
                r[0]=i
        return r


        