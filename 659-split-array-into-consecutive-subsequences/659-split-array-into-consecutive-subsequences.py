class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        
        n=len(nums)
        
        left=Counter(nums)
        end=Counter()
        
        for i in nums:
            
            if left[i]==0:
                continue
            
            if end[i-1]>0:
                
                left[i]-=1
                end[i-1]-=1
                end[i]+=1
            elif left[i+1]>0 and left[i+2]>0:
                left[i]-=1
                left[i+1]-=1
                left[i+2]-=1
                end[i+2]+=1
            else:
                return False
        
        return True
                
        
        '''
        
        
        0 1 2 3 4 5 6
                    x 
        
        
        
        
        
        
        '''
        