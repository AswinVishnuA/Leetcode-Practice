class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d=defaultdict(int)
        # print(d)
        n=len(nums)
        d[0]=1
        res=0
        cur=0
        for i in range(n):
            cur+=nums[i]
            res+=d[cur-k]
            d[cur]+=1
        
        # print(d)
        return res
            
        