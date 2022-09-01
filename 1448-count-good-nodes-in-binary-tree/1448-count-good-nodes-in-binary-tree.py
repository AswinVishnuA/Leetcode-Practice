# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        
        def dfs(cur,maxval):
            
            if not cur:
                return 0
            # print(cur.val,maxval)
            if cur.val>=maxval:

                left=dfs(cur.left,cur.val)
                right=dfs(cur.right,cur.val)
                
                return left+right+1
            
            left=dfs(cur.left,maxval)
            right=dfs(cur.right,maxval)

            return left+right
        
        return dfs(root,float("-inf"))
            
            
            
        