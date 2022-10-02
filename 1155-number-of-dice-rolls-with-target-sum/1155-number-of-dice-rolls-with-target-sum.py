class Solution:
    @lru_cache(None)
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # print(n,k,target)
        if n==0 and target==0:
            return 1
        
        if  n==0 or target<0:
            return 0
        ans=0
        for i in range(1,k+1):
            # print(i,target)
            ans=(ans+self.numRollsToTarget(n-1,k,target-i))%(1000000007)
        
        return ans%(1000000007)
        
        
        