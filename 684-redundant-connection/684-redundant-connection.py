class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        
        adj=defaultdict(list)
        
        
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        print(adj)
        vis=set()
        
        ans=set()
        
        start=[-1]
        
        def dfs(node,prev):
            
            if adj[node]:
                # print(node,prev)
                if node in vis:
                    start[0]=node
                    return
                
                vis.add(node)
                
                for nbr in adj[node]:
                    if nbr==prev:
                        continue
                    if len(ans)==0:
                        dfs(nbr,node)
                    
                    if start[0]!=-1:
                        ans.add(node)
                    if node==start[0]:
                        start[0]=-1
                            
        

        dfs(1,None)
        
        for edge in reversed(edges):
            if edge[0] in ans and edge[1] in ans:
                return edge
        
        
        
        
        