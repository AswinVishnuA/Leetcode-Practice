class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        
        adj=defaultdict(list)
        
        for a,b in sorted(tickets)[::-1]:
            adj[a]+=b,
        
        ans=[]
        
        def visit(cur):
            
            while adj[cur]:
                visit(adj[cur].pop())
            
            ans.append(cur)
        
        visit("JFK")
        
        return ans[::-1]
    
            
            
            
            
        