# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def flatten(self, root1: Optional[TreeNode]) -> None:
        
        
        prev=[None]
        def dfs(root):
            if not root:
                return None
            
            dfs(root.right)
            dfs(root.left)
            
            root.right=prev[0]
            
            root.left=None
            
            prev[0]=root
            
        
        dfs(root1)
        