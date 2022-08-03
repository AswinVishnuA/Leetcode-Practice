class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        n=len(edges)
        
        adj=defaultdict(list)
        
        for i in range(n):
            if edges[i]!=-1:
                adj[i].append(edges[i])
                
        vis=defaultdict(int)
        
        dp=defaultdict(int)
        
        maxlength=[0]
        
        def dfs(cur,l):
            
            if vis[cur]==-1:
                maxlength[0]=max(maxlength[0],l-dp[cur])
                vis[cur]=1
                return False
            
            if vis[cur]==0:
                
                dp[cur]=l
                vis[cur]=-1
                for nb in adj[cur]:
                    if not dfs(nb,l+1):
                        return False
                
                vis[cur]=1
            return True
            
            
        
        check=True
        for i in range(n):
            if i not in vis:
                check= dfs(i,1) and check
        print(dp)
        if check:
            return -1
        else:
            return maxlength[0]
                    
                    
        