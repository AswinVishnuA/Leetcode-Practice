class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        n=len(matrix)
        m=len(matrix[0])
        
        for i in range(m):
            val=matrix[0][i]
            # print(val,0,i)
            x=1
            y=i+1
            
            while x<n and y<m:
                # print(val,x,y)
                if matrix[x][y]!=val:
                    return False
            
                x+=1
                y+=1
                
        for i in range(n):
            val=matrix[i][0]
            # print(val,0,i)
            y=1
            x=i+1
            
            while x<n and y<m:
                # print(val,x,y)
                if matrix[x][y]!=val:
                    return False
            
                x+=1
                y+=1
        return True
        
        