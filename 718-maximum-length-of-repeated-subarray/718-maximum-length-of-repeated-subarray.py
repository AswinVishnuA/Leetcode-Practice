class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        m=len(nums1)
        n=len(nums2)
        
        dp=[0]*(m+1)
        
        ans=0
        for i in range(1,n+1):
            prev=dp.copy()
            for j in range(1,m+1):
                if nums1[j-1]==nums2[i-1]:
                    dp[j]=prev[j-1]+1
                else:
                    dp[j]=0
            
                ans=max(ans,dp[j])
                    
        
        return ans
        
        
        