class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        mod= 7 + 10**9
        
        @lru_cache(None)
        def solve(i,prev):
            
            if i==n:
                return 1
           
        
            if prev=='a':
                return solve(i+1,"e")
            elif prev=='e':
                return (solve(i+1,"a")+solve(i+1,"i"))
            elif prev=='o':
                return (solve(i+1,"i")+solve(i+1,"u"))
            elif prev=='u':
                return solve(i+1,"a")
            else:
                return (solve(i+1,"a")+solve(i+1,"e")+solve(i+1,"o")+solve(i+1,"u"))
        ans=0
        for c in "aeiou":
            ans=(ans+solve(1,c))%mod
        
        return ans
        