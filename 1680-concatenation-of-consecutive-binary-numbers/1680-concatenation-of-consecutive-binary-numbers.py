class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binary = ''
        for i in range(1, n + 1):
            binary = binary + bin(i).split('b')[1]
        decimal = int(binary, 2)
        return decimal % 1000000007
    
#         cur=n
#         length=len(bin(cur))-2

#         MOD=(10**9 + 7)
        
#         curLen=0
#         ans=0
#         for i in range(n,0,-1):
#             ans= (ans+(i<<curLen))%MOD
#             curLen+=length
#             if i&(i-1)==0:
#                 length-=1
            
#         return ans % MOD
            
        