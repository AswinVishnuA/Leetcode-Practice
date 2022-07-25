class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        n=len(nums)
        low=0
        high=len(nums)-1
        ans1=0
        while low<=high:
            
            mid=low+(high-low)//2
            
            print
            if nums[mid]==target:
                high=mid-1
                ans1=mid
            elif nums[mid]>target:
                high=mid-1
                ans1=high
            else:
                low=mid+1
                ans1=low
        
        # print(low,high,ans1)
        if ans1>=n or ans1<0 or nums[ans1]!=target:
            return [-1,-1]
        
        low=0
        high=len(nums)-1
        ans2=0
        while low<=high:
            
            mid=low+(high-low)//2
            if nums[mid]==target:
                low=mid+1
                ans2=mid
            elif nums[mid]>target:
                high=mid-1
                ans2=high
            else:
                low=mid+1
                ans2=low
        
        # print(low,high,ans2)
        
        return [ans1,ans2]
        
                
        