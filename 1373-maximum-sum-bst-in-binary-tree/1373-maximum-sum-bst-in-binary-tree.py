# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        ans=[0]
        
        @lru_cache(None)
        def isbst(cur,leftl,rightl):
            
            if not cur:
                return True
            
            if leftl<cur.val<rightl:
                
                return isbst(cur.left,leftl,cur.val) and isbst(cur.right,cur.val,rightl) 
            
            return False
        
        @lru_cache(None)
        def findsum(cur):
            
            if not cur:
                return 0
            
            return cur.val + findsum(cur.left) + findsum(cur.right)
        
        
        def dfs(cur):
            
            if cur:
                
                if isbst(cur,float("-inf"),float("inf")):
                    
                    ans[0]=max(ans[0],findsum(cur))
                
                
                dfs(cur.left)
                dfs(cur.right)

                    
                    
            
            
            
        
        
        
        dfs(root)
        
        return ans[0]