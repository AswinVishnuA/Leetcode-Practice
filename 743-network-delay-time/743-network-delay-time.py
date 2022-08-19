class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        
        vis=set()
        
        adj=defaultdict(list)
        
        for edge in times:
            adj[edge[0]].append([edge[-1],edge[1]])
            # adj[edge[1]].append([edge[-1],edge[0]])
        
        vis.add(k)
        
        pq=[[0,k]]
        
        heapify(pq)
        
        maxDist=0
        while len(pq):
          
            curDist,node=heappop(pq)
            maxDist=max(maxDist,curDist)
            vis.add(node)
            if len(vis)==n:
                break
            # print(curDist,node,vis,pq,adj[node])

            
            for dist,nbr in adj[node]:
                if nbr not in vis:
                    heappush(pq,[curDist+dist,nbr])
        
        if len(vis)!=n:
            return -1
        return maxDist
        
        
            
        
        