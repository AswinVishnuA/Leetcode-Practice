class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        s=set()
        
        n=len(colors)
        prev=0
        cost=0
        for i in range(1,n):
            if colors[i]==colors[i-1]:
                if neededTime[prev]<neededTime[i]:
                    cost+=neededTime[prev]
                    prev=i
                else:
                    cost+=neededTime[i]
            else:
                prev=i
        
        return cost
                    
                    
        
        