class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur_max=0
        sum_now=0
        n=len(nums)
        for i in range(n):
            sum_now+=nums[i]
            
            if sum_now<0:
                sum_now=0
                continue
            if sum_now>cur_max:
                cur_max=sum_now
        
        return cur_max if cur_max!=0 else max(nums)