class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
        rows=len(matrix)
        columns=len(matrix[0])
        
        ans=float("-inf")
        
        for i in range(columns):
            
            sums=[0 for _ in range(rows)]
            
            for j in range(i,columns):
                
                for r in range(rows):
                    sums[r]+=matrix[r][j]
                    
                # print(i,j)
                
                cum_sum = [0]
                cum, max_sum = 0, float('-inf')
                for item in sums:
                    cum += item
                    left = bisect.bisect_left(cum_sum, cum - k)
                    if left < len(cum_sum):
                        max_sum = max(max_sum, cum - cum_sum[left])
                    bisect.insort(cum_sum, cum)

                ans = max(ans, max_sum)
                    
                    
                    
        return ans
                    
                    
         
                        
        