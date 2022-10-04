# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        def dfs(root,targetSum):
            
            if not root:
                return False
            
            if root.right==None and root.left==None:
                return targetSum==root.val
            curSum=targetSum-root.val
            return dfs(root.left,curSum) or dfs(root.right,curSum)
        
        
        return dfs(root,targetSum)