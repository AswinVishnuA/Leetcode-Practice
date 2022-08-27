class Solution:
    def numSubmatrixSumTarget(self, A: List[List[int]], target: int) -> int:
        
        m, n = len(A), len(A[0])
        
        res=0
        for i in range(n):
            
            sums=[0 for _ in range(m)]
            
            for j in range(i,n):
                
                for k in range(m):
                    sums[k]+=A[k][j]
                
                d=defaultdict(int)
                d[0]=1
                curSum=0
                for val in sums:
                    curSum+=val
                    res+=d[curSum-target]
                    d[curSum]+=1
                    
        return res
                    
                    
                