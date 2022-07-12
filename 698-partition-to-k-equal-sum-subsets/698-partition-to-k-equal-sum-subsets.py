class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        
        subsets=[0 for i in range(k)]
        
        length=len(nums)
        
        
        summ=sum(nums)
        
        if summ % k!=0:
            return False
        tar=summ//k
        
        nums.sort(reverse=True)
        
        if nums[0]>tar:
            return False
        
        def dfs(ss,n):
            if n==length:
                
                for i in range(1,k):
                    if ss[i]!=ss[i-1]:
                        return False
                
                return True
            
            
            for i in range(k):
                
                if ss[i]+nums[n]>tar:
                    continue
                
                j=i-1
                
                while j>=0:
                    if ss[i]==ss[j]:
                        break
                    j-=1
                
                if j!=-1:
                    continue
                
                ss[i]+=nums[n]
                
                if dfs(ss,n+1):
                    return True
                ss[i]-=nums[n]
            
            return False
        
        return dfs(subsets,0)
        