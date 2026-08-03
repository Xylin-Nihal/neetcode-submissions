class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        h={}
        m=0
        for i in range(len(wall)):
            j=0
            while j<len(wall[i])-1:
                if j>0:

                    wall[i][j]=wall[i][j]+wall[i][j-1]
                h[wall[i][j]]=h.get(wall[i][j],0)+1
                m=max(m,h[wall[i][j]])
                j+=1
        return len(wall)-m