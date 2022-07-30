class Solution:
    def findOrder(self, nc: int, pr: List[List[int]]) -> List[int]:
        
        adj=defaultdict(list)
        
        for a,b in pr:
            adj[a].append(b)
        
        dp=defaultdict(list)
        vis=defaultdict(int)
        flag=[True]
        ans=[]
        def dfs(cur):
            
            if vis[cur]==-1:
                return False

            if vis[cur]==0:
                vis[cur]=-1

                for ns in adj[cur]:
                    if not dfs(ns):
                        return False

                ans.append(cur)
                vis[cur]=1

            return True
        
        for i in range(nc):
            if i not in vis:
                if not dfs(i):
                    return []
        
        return ans
                    
        