class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        
        def solve(i,curSet):
            # print(i,curSet)
            if i==len(arr):
                return 0
            
            
            s=set(list(arr[i]))
            
            if len(s)!=len(arr[i]):
                return solve(i+1,curSet)
            
            if s-curSet==s:
                return max(solve(i+1,curSet),len(arr[i])+solve(i+1,curSet.union(s)))
            
            return solve(i+1,curSet)
        
        s=set()
        return solve(0,s)
        