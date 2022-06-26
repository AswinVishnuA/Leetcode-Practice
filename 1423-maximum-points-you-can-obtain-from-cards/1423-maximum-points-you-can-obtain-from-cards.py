class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        
        n=len(cp)
        
        sum_arr=[]
        sum_val=0
        for i in range(n):
            sum_val+=cp[i]
            sum_arr.append(sum_val)
        
        ans=0
        
        for a in range(k+1):
            b=k-a
            
            right_sum=sum_arr[n-1]-sum_arr[n-1-b]
            if a!=0:
                left_sum=sum_arr[a-1]
            else:
                left_sum=0
            
            ans=max(ans,left_sum+right_sum)
        
        return ans
            
            
            
        