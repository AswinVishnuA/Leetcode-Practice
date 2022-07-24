class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        
        row=0
        m=len(mat)
        n=len(mat[0])
        while row<m:
            if mat[row][0]<=target<=mat[row][-1]:
                low=0
                high=n-1

                print(row)
                while low<=high:

                    mid = (low+high)//2

                    if mat[row][mid]==target:
                        return True

                    elif mat[row][mid]<target:
                        low=mid+1
                    else:
                        high=mid-1

                print(high,low)
            row+=1
        
        if row==m:
            return False
        
        
        return mat[row][low]==target
        