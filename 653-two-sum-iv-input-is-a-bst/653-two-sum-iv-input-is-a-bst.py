# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        
        arr=[]
        
        
        def dfs(root):
            
            if root:
                dfs(root.left)
                
                arr.append(root.val)
                dfs(root.right)
        
        def twoSum():
            
            l=0
            r=len(arr)-1
            
            while l<r:
                curSum=arr[l]+arr[r]
                
                if curSum==k:
                    return True
                
                elif curSum<k:
                    l+=1
                else:
                    r-=1
            return False
        
        dfs(root)
        print(arr)
        return twoSum()
        
            
            
                
                
        