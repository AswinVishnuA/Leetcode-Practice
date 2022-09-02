# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q=deque([])
        
        q.append(root)
        ans=[]
        while len(q):
            size=len(q)
            curSum=0
            curCount=size
            while size:
                
                cur=q.popleft()
                
                curSum+=cur.val
                
                if cur.left:
                    q.append(cur.left)
                
                if cur.right:
                    q.append(cur.right)
                    
            
                size-=1
            ans.append(curSum/curCount)
        return ans
        