class Solution:
    def searchMatrix(self, mat: List[List[int]], tar: int) -> bool:
        
        nr,nc = len(mat),len(mat[0])
        
        u,d=0,nr-1
        
        while u<d:
            m=u+(d-u)//2
            
            if mat[m][0]<=tar<=mat[m][-1]:
                u=m
                break
            elif mat[m][0]<tar:
                u=m+1
            else:
                d=m
                
        l,r=0,nc-1
        
        while l<r:
            m=l+(r-l)//2
            
            if  mat[u][m]<tar:
                l=m+1
            else:
                r=m
        print(u,l)
        return mat[u][l]==tar 
        
        
        