class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        
        l=0
        r=len(nums)
        while l<r:
            m=l+(r-l)//2
            if nums[m]<tar:
                l=m+1
            else:
                r=m
        return l if l<len(nums) and nums[l]==tar else -1
        