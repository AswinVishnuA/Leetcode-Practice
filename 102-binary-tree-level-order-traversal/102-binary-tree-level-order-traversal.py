# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans=[]
        
        que=deque([root])
        
        while len(que)!=0:
            size=len(que)
            lvl=[]
            while(size):
                cur=que.popleft()
                lvl.append(cur.val)
                
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                
                size-=1
            ans.append(lvl)
        
        return ans
                