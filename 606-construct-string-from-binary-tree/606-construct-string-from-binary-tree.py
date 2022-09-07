# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        ans=""
        
        
        def dfs(curNode):
            nonlocal ans
            
            ans+="("+str(curNode.val)
            
            if not curNode.left and not curNode.right:
                ans+=")"
                return
            elif not curNode.left:
                ans+="()"                        
                dfs(curNode.right)
            elif not curNode.right:
                dfs(curNode.left)
            else:
                dfs(curNode.left)
                dfs(curNode.right)
                
            
            ans+=")"
            
            return
        
        dfs(root)
        return ans[1:-1]
            
        