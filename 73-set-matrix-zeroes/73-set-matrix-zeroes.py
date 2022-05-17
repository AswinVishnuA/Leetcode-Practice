class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        zero_rows=set()
        zero_cols=set()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for i in range(len(mat)):
            if i in zero_rows:
                for j in range(len(mat[0])):
                    mat[i][j]=0
        for j in range(len(mat[0])):
            if j in zero_cols:
                for i in range(len(mat)):
                    mat[i][j]=0
        return mat
        