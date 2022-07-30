class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        
        d=defaultdict(int)
        d2=defaultdict(dict)

        
        for word in words1:
            if word in d2:
                continue
            for c in word:
                if c not in d2[word]:
                    d2[word][c]=1
                else:
                    d2[word][c]+=1
        
        for word in words2:
            tmp={}
            for c in word:
                if c not in tmp:
                    tmp[c]=1
                else:
                    tmp[c]+=1
            
            for c in tmp:
                if c not in d:
                    d[c]=tmp[c]
                else:
                    d[c]=max(d[c],tmp[c])
                    
                
        
        # print(d)
        ans=[]
        for word in words1:
            flag=True
            for c in d:
                if c not in d2[word] or d[c]>d2[word][c]:
                    flag=False
                    break
            
            if flag:
                ans.append(word)
        
        return ans