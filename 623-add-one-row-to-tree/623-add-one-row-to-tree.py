# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth==1:
            return TreeNode(val,root,None)
        
        q=deque([])
        q.append(root)
        level=1
        while len(q):
            size=len(q)
            if level+1==depth:
                
                for node in q:
                    # print(node.val)
                    node.left=TreeNode(val,node.left,None)
                    node.right=TreeNode(val,None,node.right)
            
            while size:
                
                curNode=q.popleft()
                
                if curNode.left:
                    q.append(curNode.left)
                
                
                if curNode.right:
                    q.append(curNode.right)
                
                size-=1
            
            level+=1
        
        
        return root
                
            
        
        