class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        
        l=0
        r=len(nums)-1
        while l<r:
            m=l+(r-l+1)//2
            if nums[m]>tar:
                r=m-1
            else:
                l=m
        return l if nums[l]==tar else -1
        