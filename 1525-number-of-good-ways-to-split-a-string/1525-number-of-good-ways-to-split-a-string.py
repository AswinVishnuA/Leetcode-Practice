class Solution:
    def numSplits(self, s: str) -> int:
        left=defaultdict(int)
        right=defaultdict(int)
        
        for c in s:
            right[c]+=1
        
        ans=0
        for c in s:
            left[c]+=1
            right[c]-=1
            if right[c]==0:
                right.pop(c)
            if len(left)==len(right):
                ans+=1
        
        return ans