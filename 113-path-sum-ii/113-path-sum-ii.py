# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        self.ans=[]
        
        def dfs(root,targetSum,curArr):
            
            if root.left==None and root.right==None:
                if targetSum==root.val:
                    curArr.append(root.val)
                    self.ans.append(curArr.copy())
                    curArr.pop()
                return 
            
            curArr.append(root.val)
            if root.left:
                dfs(root.left,targetSum-root.val,curArr)
            if root.right:
                dfs(root.right,targetSum-root.val,curArr)
            curArr.pop()
            return
        
        dfs(root,targetSum,[])
        
        return self.ans
                
        