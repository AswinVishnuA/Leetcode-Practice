# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        
        i=[0]
        
        def dfs(leftl,rightl):
            # print(leftl,rightl)
            if i[0]==len(preorder):
                return None
            
            
            if leftl<preorder[i[0]]<rightl:
                root=TreeNode(preorder[i[0]])
                i[0]+=1
                root.left=dfs(leftl,root.val)
                
                
                root.right=dfs(root.val,rightl)
                
                return root
            
            return None
            
        
        return dfs(float("-inf"),float("inf"))
                
                
            
        