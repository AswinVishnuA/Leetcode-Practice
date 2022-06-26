class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        
        n= len(nums1)
        
        max_diff=0
        cur_sum=0
        for i in range(n):
            
            diff=nums1[i]-nums2[i]
            
            cur_sum+=diff
            
            max_diff=max(max_diff,cur_sum)
            
            cur_sum=max(cur_sum,0)
        
        ans_1=sum(nums2)+max_diff
        
        max_diff=0
        cur_sum=0
        for i in range(n):
            
            diff=nums2[i]-nums1[i]
            
            cur_sum+=diff
            
            max_diff=max(max_diff,cur_sum)
            
            cur_sum=max(cur_sum,0)
        
        ans_2=sum(nums1)+max_diff
        
        return max(ans_1,ans_2)
        
            
                
        