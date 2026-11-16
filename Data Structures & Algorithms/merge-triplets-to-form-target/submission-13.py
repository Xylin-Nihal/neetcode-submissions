class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        current=[0,0,0]
        for i,j,k in triplets:
            if [i,j,k]==target:
                return True
            if i>target[0] or j>target[1] or k>target[2]:
                continue
            current=[max(current[0],i),max(current[1],j),max(current[2],k)]
            if current==target:
                return True
        return False