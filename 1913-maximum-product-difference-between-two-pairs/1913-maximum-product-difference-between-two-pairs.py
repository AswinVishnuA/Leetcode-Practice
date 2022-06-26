class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        
        min_1=float("inf")
        min_2=float("inf")
        max_1=0
        max_2=0
        min_idx=0
        max_idx=0
        for i in range(len(nums)):
            if nums[i]>max_1:
                max_1=nums[i]
                max_idx=i                
            if nums[i]<min_1:
                min_1=nums[i]
                min_idx=i
        print(max_1,min_1)
        for i in range(len(nums)):
            if i== max_idx or i==min_idx:
                continue
            if nums[i]>max_2:
                max_2=nums[i]
            if nums[i]<min_2:
                min_2=nums[i]
        print(max_2,min_2)
 
        
        return max_1*max_2-min_1*min_2