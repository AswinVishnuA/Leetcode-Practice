# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return None
        ans=[]
        
        que=deque([root])
        
        while len(que)!=0:
            
            size=len(que)
            first=True
            while(size):
                
                cur=que.popleft()
                
                if first:
                    ans.append(cur.val)
                    first=False
                
                if cur.right:
                    que.append(cur.right)
                if cur.left:
                    que.append(cur.left)
                
                size-=1
                    
        
        return ans
        