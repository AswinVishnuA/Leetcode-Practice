class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        
        s=set()
        ans=0
        for i in rolls:
            s.add(i)
            
            if len(s)==k:
                ans+=1
                s=set()
        
        return ans+1
        