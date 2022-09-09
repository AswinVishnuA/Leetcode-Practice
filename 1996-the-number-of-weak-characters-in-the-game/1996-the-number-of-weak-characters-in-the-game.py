class Solution:
    def numberOfWeakCharacters(self, prpts: List[List[int]]) -> int:
        
        
        prpts.sort(key=lambda x:(x[0],-x[1]))
        
        stack=[]
        ans=0
        for a,d in prpts:
            while stack and stack[-1]<d:
                ans+=1
                stack.pop()
            
            stack.append(d)
        
        return ans
        
        
        
        