class Solution:
    def findOrder(self, nc: int, pr: List[List[int]]) -> List[int]:
        
        adj=defaultdict(list)
        
        for a,b in pr:
            adj[b].append(a)
        
        degree=[0 for i in range(nc)]
        
        for v in adj:
            for nbr in adj[v]:
                degree[nbr]+=1
        ans=[]
        
        for i in range(nc):
            
            for j in range(nc+1):
                
                if j==nc:
                    break
                
                if degree[j]==0:
                    break
            
            if j==nc:
                return []
            
            degree[j]-=1
            ans.append(j)
            for nbr in adj[j]:
                degree[nbr]-=1
            
        
        return ans
                    
        