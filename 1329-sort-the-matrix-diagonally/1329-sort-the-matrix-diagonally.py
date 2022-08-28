class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        m=len(mat)
        n=len(mat[0])
        
        for i in range(n):
            
            r=0
            c=i
            arr=[]
            while c<n and r<m:
                arr.append(mat[r][c])
                r+=1
                c+=1

            arr.sort()
            
            r=0
            c=i
            count=0
            while c<n and r<m:
                mat[r][c]=arr[count]
                r+=1
                c+=1
                count+=1
        
        for i in range(1,m):
            
            r=i
            c=0
            arr=[]
            while c<n and r<m:
                arr.append(mat[r][c])
                r+=1
                c+=1

            arr.sort()
            
            r=i
            c=0
            count=0
            while c<n and r<m:
                mat[r][c]=arr[count]
                r+=1
                c+=1
                count+=1
            
        return mat
        