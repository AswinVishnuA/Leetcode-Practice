class Solution:
    def isBipartite(self, g: List[List[int]]) -> bool:
        
        
        
        vis=defaultdict(int)
        def bfs():
            while len(q)!=0:

                cur,s=q.popleft()

                vis[cur]=s


                for nbs in g[cur]:

                    if nbs in vis:
                        if vis[nbs]==s:
                            return False
                    else:
                        q.append([nbs,not s])
                        
            return True
        for i in range(len(g)):
            if i not in vis:
                q=deque([])
                q.append([i,0])
                if bfs()==False:
                    return False
        return True
                
                

                    
            
            
        
        