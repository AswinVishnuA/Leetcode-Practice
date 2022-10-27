class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        d=defaultdict(int)
        
        
        a,b=[],[]
        
        n=len(img1)
        
        
        for i in range(n):
            for j in range(n):
                
                if img1[i][j]==1:
                    a.append((i,j))
                
                if img2[i][j]==1:
                    b.append((i,j))
                    
        ans=0
        for p1 in a:
            for p2 in b:
                
                change=(p1[0]-p2[0],p1[1]-p2[1])
                
                d[change]+=1
                
                ans=max(ans,d[change])
        
        return ans
                
                
                
                
        