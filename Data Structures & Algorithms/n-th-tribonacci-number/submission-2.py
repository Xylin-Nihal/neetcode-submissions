class Solution:
    
    def tribonacci(self, n: int) -> int:
        cache={0:0,1:1,2:1}
        if n in cache:
            return cache[n]
        #cache[n]=self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        if n>=3:
            for i in range(3,n+1):
                cache[i]=cache[i-1]+cache[i-2]+cache[i-3]
        return cache[n]