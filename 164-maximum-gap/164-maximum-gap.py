class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        hi,lo=max(nums),min(nums)
        n=len(nums)
        if n<=2 or lo==hi: return hi-lo
        d={i:[] for i in range(n-1)}
        
        for val in nums:
            idx= n-2 if val==hi else (val-lo)*(n-1)//(hi-lo)
            
            d[idx].append(val)
            
        cand=[[min(d[i]),max(d[i])] for i in range(n-1) if d[i]]
        
        return max(x[0]-y[1] for x,y in zip(cand[1:],cand))
            
            
        