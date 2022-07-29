class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        
        n=len(words)
        ans=[]
        for word  in words:
            d={}
            d2={}
            i=0
            flag=True
            for c in pattern:
                # print(c,word[i],d,d2)
                if c not in d:
                    if word[i] not in d2:
                        d[c]=word[i]
                        d2[word[i]]=c
                    else:
                        flag=False
                        break
                elif d[c]!=word[i] or d2[word[i]]!=c:
                    flag=False
                    break
                
                i+=1
            
            if flag:
                ans.append(word)
        
        
        return ans
                
            
        