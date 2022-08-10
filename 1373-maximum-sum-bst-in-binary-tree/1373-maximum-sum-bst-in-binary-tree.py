# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        ans=[0]
        
#         @lru_cache(None)
#         def isbst(cur,leftl,rightl):
            
#             if not cur:
#                 return True
            
#             if leftl<cur.val<rightl:
                
#                 return isbst(cur.left,leftl,cur.val) and isbst(cur.right,cur.val,rightl) 
            
#             return False
        
#         @lru_cache(None)
#         def findsum(cur):
            
#             if not cur:
#                 return 0
            
#             return cur.val + findsum(cur.left) + findsum(cur.right)
        
        @lru_cache(None)
        def checkandsum(cur,leftl,rightl):
            
            if not cur:
                return True,0
            
            if leftl<cur.val<rightl:
                leftb,sumvall=checkandsum(cur.left,leftl,cur.val)
                rightb,sumvalr=checkandsum(cur.right,cur.val,rightl)
                
                if leftb and rightb:
                    return True,cur.val+sumvall+sumvalr
            
            return False,0
                    
                
            
            return False
        
        def dfs(cur):
            
            if cur:
                
                check,sumval=checkandsum(cur,float("-inf"),float("inf"))
                
                if check:
                    ans[0]=max(ans[0],sumval)
                
                
                dfs(cur.left)
                dfs(cur.right)

        
        dfs(root)
        
        return ans[0]