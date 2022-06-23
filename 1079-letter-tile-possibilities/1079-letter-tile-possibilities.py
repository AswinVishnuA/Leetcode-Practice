class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        s=set()
        def dfs(a,t):
            if a not in s:
                s.add(a)
                                        
            for i in range(len(t)):
                dfs(a+t[i],t[:i]+t[i+1:])
        
        dfs("",tiles)
        return len(s)-1
                
        