# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        self.ans=root
        
        
        def dfs(cur):
            
            if cur==None:
                return
            
            if ((cur.val>=p.val and cur.val<=q.val) or (cur.val>=q.val and cur.val<=p.val)):
                self.ans=cur
            elif cur.val>p.val and cur.val>q.val:
                dfs(cur.left)
            else:
                dfs(cur.right)
        
        dfs(root)
        return self.ans
                
        