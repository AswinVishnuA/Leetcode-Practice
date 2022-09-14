# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        d=defaultdict(int)
        
        self.ans=0
        
        def dfs(curNode,count):
            
            if not curNode:
                return
            
            count[curNode.val]+=1
            
            if curNode.right==None and curNode.left==None:
                # print(count)
                total=0
                for key in count:
                    total+=count[key]
                        
                if total%2==0:
                    
                    for key in count:
                        val=count[key]
                        
                        if val% 2!=0:
                            count[curNode.val]-=1
                            return
                else:
                    singles=0
                    for key in count:
                        val=count[key]
                        if val%2==1:
                            singles+=1
                        
                        if singles>1:
                            count[curNode.val]-=1
                            return
                self.ans+=1
                # print(self.ans)
            
            dfs(curNode.left,count)
            dfs(curNode.right,count)
            count[curNode.val]-=1
            if count[curNode.val]==0:
                count.pop(curNode.val)
            return
        
        dfs(root,d)
        
        return self.ans
            
                    
                
        