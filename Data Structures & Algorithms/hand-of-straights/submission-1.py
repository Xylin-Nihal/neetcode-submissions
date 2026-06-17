class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        h={}
        c=0
        for i in hand:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        while 1:
            x=min(h)
            if c==len(hand):
                return True
            if h[x]>0:
                for i in range(0,groupSize):
                    if x+i in h and h[x+i]>0:
                        h[x+i]-=1
                        print(h[x+i],x+i,i)
                    else:
                        return False
                    c+=1
            else:
                h.pop(x)
