class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        d=defaultdict(lambda :0)
        for i in range(len(nums)):
            d[nums[i]]+=1
            if d[nums[i]]==len(nums)//2:
                return nums[i]
        
        
        