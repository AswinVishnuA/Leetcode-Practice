class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        st=set(list(s))
        ans=0
        for word in words:
            
            if set(list(word)) - st !=set():
                continue
                
            
            i=len(s)-1
            j=len(word)-1
            
            while i>=0:
                
                if word[j]==s[i]:
                    j-=1
                    i-=1
                else:
                    i-=1
                
                if j==-1:
                    ans+=1
                    break
        
        return ans
        