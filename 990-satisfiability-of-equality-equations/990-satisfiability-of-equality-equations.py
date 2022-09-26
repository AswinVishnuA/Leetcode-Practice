class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        
        
        
        adj=defaultdict(list)
        
        for eqn in equations:
            if eqn[1:3]=="==":
                adj[eqn[0]].append(eqn[3])
                adj[eqn[3]].append(eqn[0])
        
        def dfs(cur,tar):
            
            if cur==tar:
                return True
            
            vis.add(cur)
            
            for nbr in adj[cur]:
                if nbr not in vis:
                    if dfs(nbr,tar):
                        return True
            
            return False
        
        
        for eqn in equations:
            if eqn[1:3]=="!=":
                fromn=eqn[0]
                vis=set()
                ton=eqn[3]
                if dfs(fromn,ton):
                    return False
        
        return True
                
        