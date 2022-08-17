class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n=len(points)
        adj=defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                
                adj[i].append(j)
        
        pq=[[0,0]]
        heapify(pq)
        
        vis=set()
        
        cost=0
        while len(pq)>0 and len(vis)!=n:
            
            curcost,cur=heappop(pq)
            if cur in vis:
                continue
            vis.add(cur)
            cost+=curcost
            # print(cur,curcost,vis,adj[cur])
            
            for nbr in adj[cur]:
                if nbr not in vis:
                    dist=abs(points[nbr][0]-points[cur][0])+abs(points[nbr][1]-points[cur][1])
                    heappush(pq,[dist,nbr])
        return cost
                
            
        