class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        length=len(strs)

        def count_bits(arr):
            c1=[]
            c0=[]
            for i in arr:
                ones=0
                for j in i:
                    if j=='1':
                        ones+=1
                c0.append(len(i)-ones)
                c1.append(ones)
            
            return c1,c0
        
        c1,c0= count_bits(strs)
        # print(c1,c0)
        @lru_cache(None)
        def solve(l,mb,nb):
            
            if l==0 or mb<0 or nb<0:
                return 0
            
            ans=0
            if c0[l-1]<=mb and c1[l-1]<=nb:
                ans=1+solve(l-1,mb-c0[l-1],nb-c1[l-1])
            
            
            ans=max(ans,solve(l-1,mb,nb))    
            
            return ans
            
        
        return solve(length,m,n)