class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n=len(arr)
        
        
        prefixs=[arr[0]]
        for i in range(1,n):
            prefixs.append(prefixs[-1]+arr[i])
        
        print(prefixs)
        
        sumval=0
        for i in range(n):
            for j in range(i,n):
                if (j-i+1)%2==1:
                    sumval+=(prefixs[j]-prefixs[i]+arr[i])
        
        return sumval
            
            
        
            
            
            
        
        
        