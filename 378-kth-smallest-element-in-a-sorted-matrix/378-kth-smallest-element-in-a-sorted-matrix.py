class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        
        m=len(mat)
        n=len(mat[0])
        
        def check(x):
            
            count=0
            for i in range(len(mat)):
                
                if mat[i][0]<=x:
                    
                    l=0
                    h=n-1
                    
                    while l<h:
                        m = l+ (h-l+1)//2
                        
                        if mat[i][m]<=x:
                            l=m
                        else:
                            h=m-1
                    
                    if mat[i][h]<=x:
                        count+=(h+1)
            return count
                        
        
        
        
        
        low=mat[0][0]
        high=mat[m-1][n-1]
        
        while low<high:
            
            mid= low + (high-low)//2
            
            if check(mid)>=k:
                high=mid
            else:
                low=mid+1
        
        return high
                
        