class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        x=[]
        res=[]
        c=0
        for i in range(len(boxes)):
            if boxes[i]=="1":
                x.append(i)
        
        for i in range(len(boxes)):
            for j in x:
                h=abs(i-j)
                
                c+=h
            res.append(c)
            c=0
        return res