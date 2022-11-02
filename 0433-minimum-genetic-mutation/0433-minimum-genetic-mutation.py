class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        adj=defaultdict(list)
        bankSet=set(bank)
        for gene in bank:
            
            for i in range(8):
                for c in "ACGT":
                    newGene=gene[:i]+c+gene[i+1:]
                    if newGene in bankSet and newGene!=gene:
                        adj[gene].append(newGene)
                        
        
        q=deque([[start,0]])
        vis=set([start])
        while q:
            cur,mut=q.popleft()
            
            for i in range(8):
                for c in "ACGT":
                    newGene=cur[:i]+c+cur[i+1:]
                    if newGene not in vis and newGene in bankSet:
                        q.append([newGene,mut+1])
                        vis.add(newGene)
                        
                        if newGene ==end:
                            return mut+1
        
        return -1
        