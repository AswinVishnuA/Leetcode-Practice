class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        n=len(tokens)
        tokens.sort()
        i,j=0,n-1
        
        cur=0
        while i<=j:
            # print(i,j,power)
            if power>=tokens[i]:
                power-=tokens[i]
                cur+=1
                i+=1
            elif cur>0 and j>i+1:
                cur-=1
                power+=tokens[j]
                j-=1
            else:
                return cur
            
        return cur
            