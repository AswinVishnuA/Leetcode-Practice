class Solution:
    def trap(self, height: List[int]) -> int:
        
        n=len(height)
        total=0
        left=0
        right=n-1
        max_right=0
        max_left=0
        while left<right:
            
            if height[left]<height[right]:
                
                if height[left]>max_left:
                    max_left= height[left]
                else:
                    total+=max_left-height[left]
                
                left+=1
            
            else:
                
                if height[right]>max_right:
                    max_right=height[right]
                else:
                    total+=max_right-height[right]
                
                right-=1
                    
        
        return total
            
        