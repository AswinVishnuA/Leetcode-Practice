# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        
        def dfs(cur):
            
            
            if not cur:
                return False
            
            
            if dfs(cur.left):
                
                if not dfs(cur.right):
                    cur.right=None
                
                return True
            else:
                cur.left=None
            
            if dfs(cur.right):
                return True
            else:
                cur.right=None
            
            if cur.val==1:
                return True
            
            return False
        
        isValid=dfs(root)
        
        return root if isValid else None
            
            
            
        