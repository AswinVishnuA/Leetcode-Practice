# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        
        def dfs(curNode,depth):
            
            if not curNode:
                return 0
            
            
            depthDict[curNode.val]=depth
            
            height=max(dfs(curNode.left,depth+1),dfs(curNode.right,depth+1))+1
            
            heightDict[curNode.val]=height-1
            
            return height
        
        heightDict,depthDict=defaultdict(int),defaultdict(int)
        dfs(root,0)
        
        
        cousins=defaultdict(list)
        
        for node,depth in depthDict.items():
            heappush(cousins[depth],(-heightDict[node],node))
        
        ans=[]
        for q in queries:
            depth=depthDict[q]
            
            if len(cousins[depth])==1:
                ans.append(depth-1)
            elif cousins[depth][0][1]==q:
                temp=heappop(cousins[depth])
                ans.append(depth-cousins[depth][0][0])
                heappush(cousins[depth],temp)
            else:
                ans.append(depth-cousins[depth][0][0])
        return ans
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        