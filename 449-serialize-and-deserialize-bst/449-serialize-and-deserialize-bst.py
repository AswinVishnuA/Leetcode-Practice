# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        ans=[]
        def solve(root):
            if root:
                ans.append(str(root.val))
                solve(root.left)
                solve(root.right)

        solve(root)
        print("result: ",ans)
        return ' '.join(ans)
        

    def deserialize(self, data1: str) -> Optional[TreeNode]:
        
        data=deque(int(val) for val in data1.split() if val)
                
          
        def solve(lb,ub):
            if data and data[0]<ub and data[0]>lb:
                val=data.popleft()
                node=TreeNode(val)
                node.left=solve(lb,val)
                node.right=solve(val,ub)
                return node
            
            
            
            
        root=solve(float('-inf'),float("inf"))
        
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans