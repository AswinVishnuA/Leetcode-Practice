# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        
        def isbst(cur,leftl,rightl):
            
            if not cur:
                return True
            
            if leftl<cur.val<rightl:
                
                return isbst(cur.left,leftl,cur.val) and isbst(cur.right,cur.val,rightl)
            
            return False
        
        
        return isbst(root,float("-inf"),float("inf"))
        