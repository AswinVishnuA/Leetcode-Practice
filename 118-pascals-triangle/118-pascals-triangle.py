class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans=[[1]]
        for i in range(1,numRows):
            temp=[1]+[ans[i-1][j]+ans[i-1][j+1] for j in range(i-1)]+[1]
            ans.append(temp)
        return ans
            
        
        