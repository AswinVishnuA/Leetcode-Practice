# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        
        preorder-> root,root->left,root->right
        
        inorder -> root->left,root,root->right
        
        [3,9,10,8,20,15,7]
        
        [10, 9,8,3,15,20,7]
        
        10, 9,8
        
        '''
        n=len(preorder)
        d={}
        for i,num in enumerate(inorder):
            d[num]=i
        global idx
        idx=0
        def solve(io,po):
            # print(io)
            global idx
            if len(io)==0 or idx==n:
                return None
            
            root= TreeNode(po[idx])
            
            for i in range(len(io)):
                if io[i]==po[idx]:
                    break
            # print(idx[0])
            idx+=1
            root.left=solve(io[:i],po)
            root.right=solve(io[i+1:],po)
            
            return root
            
        
        
        return solve(inorder,preorder)
        