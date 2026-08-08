class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i=0
        c=0
        while 1:
            if tickets[i]==0:
                i=(i+1)%len(tickets)
                continue
            tickets[i]-=1
            c+=1
            if tickets[k]==0:
                return c
            i=(i+1)%len(tickets)
            