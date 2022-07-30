class Solution:
    def canFinish(self, nc: int, pr: List[List[int]]) -> bool:
        
        adj=defaultdict(list)
        for a,b in pr:
            adj[a].append(b)
        
        
        vis=defaultdict(int)

        def dfs(cur):
            
            if adj[cur]:
                
                if vis[cur]==1:
                    return True
                elif vis[cur]==-1:
                    return False
                
                vis[cur]=-1
                    
                for rs in adj[cur]:
                    if not dfs(rs):
                        return False
                vis[cur]=1
                
            return True
            
        for i in range(nc):
            # print(i)
            if not dfs(i):
                return False
            
        return True
                    
                
                
                
            
        