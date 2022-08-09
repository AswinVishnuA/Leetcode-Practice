class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        
        
        arr.sort()
        arr=arr[::-1]
        d={v:i for i,v in enumerate(arr)}
        n=len(arr)
        # print(arr)
        @lru_cache(None)
        def solve(i):
            
            if i==n:
                return 0
            
            count=1
            for j in range(i+1,n):
                q=arr[i]/arr[j]
                
                if q in d:
                    count=(count+solve(j)*solve(d[int(q)]))% (7 + 10**9)
                    
            # print(i,count)
            return count % (7 + 10**9)
        
        ans=0
        for i in range(n):
            ans=(ans+solve(i))% (7 + 10**9)
        return ans
                
        