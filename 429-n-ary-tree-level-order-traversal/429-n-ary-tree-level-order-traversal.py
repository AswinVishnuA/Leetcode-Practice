"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        q=deque([root])
        ans=[]
        while len(q):
            
            size=len(q)
            
            temp=[]
            
            while size:
                
                cur=q.popleft()
                temp.append(cur.val)
                
                for child in cur.children:
                    q.append(child)
                    
                
                
                size-=1
            ans.append(temp)
        
        return ans
        
        