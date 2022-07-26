# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root==None:
            return None
        
        
        ans=[None]
        
        def dfs(cur,count):
            
            if cur==None:
                return 0
            
            # print(cur.val,count,ans[0])
            
            
            if cur==p or cur==q:
                count+=1
                
                if count==2:
                    ans[0]= p if cur==q else q
                    print(ans)
                    return count
                elif count==1:
                    return max(1+dfs(cur.left,count),1+dfs(cur.right,count))
                
            a=dfs(cur.left,count)
            b=dfs(cur.right,count)
            # print(a,b)
            if a==1 and b==1:
                       ans[0]=cur
                       return 0
            
            return  max(a,b)
        
        
        
        dfs(root,0)
        return ans[0]
        