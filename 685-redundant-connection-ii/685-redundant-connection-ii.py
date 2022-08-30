class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        
        n=len(edges)
        parent=defaultdict(int)
        sus1=-1
        
        for i,edge in enumerate(edges):
            a,b=edge
            if parent[b]==0:
                parent[b]=a
            else:
                sus1=i
                break
        
        sus2=-1
        
        
        obj=UnionFind(n)
        
        for i,edge in enumerate(edges):
            a,b=edge
            if i==sus1:
                continue
            
            isCycle=obj.union(a,b)
            
            if isCycle:
                sus2=i
                break
        print(sus1,sus2)
        if sus1==-1:
            return edges[sus2]
        
        if sus2==-1:
            return edges[sus1]
        else:
            return [parent[edges[sus1][1]],edges[sus1][1]]
        
class UnionFind:
    
    def __init__(self,n):
        
        self.par=[i for i in range(n+1)]
        self.rank=[1 for i in range(n+1)]
        
    def find(self,x):
        if self.par[x]==x:
            return x
        self.par[x]=self.find(self.par[x])
        return self.par[x]
    
    def union(self,a,b):
        
        parA=self.find(a)
        parB=self.find(b)
        
        if parA==parB:
            return True
        elif self.rank[parA]<self.rank[parB]:
            self.par[parA]=parB
        else:
            self.par[parB]=parA
        
        return False
        
        
        
            
                
                
            
            
                
                    
                    
        