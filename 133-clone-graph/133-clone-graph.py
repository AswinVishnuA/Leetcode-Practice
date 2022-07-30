"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""



class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        vis=dict()
        
        
        def dfs(root):
            
            if not root:
                return None
            
            if root.val in vis:
                return vis[root.val]
            
            newNode=Node(val=root.val)
            vis[root.val]=newNode
            
            
            newnbs=[]
            for nbs in root.neighbors:
                newnbs.append(dfs(nbs))
            
            newNode.neighbors=newnbs
            
            return newNode
            
        
        
        
        return dfs(node)
        
        
        