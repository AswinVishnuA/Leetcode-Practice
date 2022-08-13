class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        
        wn=len(words[0])
        lenwd=len(words)
        d=defaultdict(int)
        
        for i in words:
            d[i]+=1
        
        
        n=len(s)
        ans=[]
        for i in range(n):
            curd=d.copy()
            count=0
            for j in range(i,n,wn):
                if j>n-wn:
                    break
    
                cur=s[j:j+wn]
                # print(curd)
                if curd[cur]>0:
                    curd[cur]-=1
                    count+=1
                else:
                    break
                # print(i,j,curd,count)

                if count==lenwd:
                    
                    ans.append(i)
                    break
        
        return ans
                
        
        
        
        
        
        
        
        """
        
        s = "barsdfoobarthefoobarthefoobarman",
        words = ["bar","foo","the"]
        
        
        """