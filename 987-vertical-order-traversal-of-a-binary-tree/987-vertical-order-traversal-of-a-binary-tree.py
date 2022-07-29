# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        arr=[]
        def dfs(cur,row,col):
            
            if cur:
                arr.append([col,row,cur.val])
                dfs(cur.left,row+1,col-1)
                dfs(cur.right,row+1,col+1)
        dfs(root,0,0)
        
        arr.sort()
        # print(arr)
        ans=[]
        cur=[arr[0][-1]]
        n=len(arr)
        i=1
        prev=arr[0][0]
        while i<n:
           
            if arr[i][0]==prev:
                cur.append(arr[i][-1])
            else:
                ans.append(cur)
                prev=arr[i][0]
                cur=[arr[i][-1]]
            i+=1
        
        if len(cur)!=0:
            ans.append(cur)
        return ans
            
            
            
            
            
            
            

            
            
            