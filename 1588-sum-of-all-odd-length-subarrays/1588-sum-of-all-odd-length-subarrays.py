class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n=len(arr)
        
        sumval=0
        
        for i in range(n):
            sumval+= (((i+1)*(n-i) + 1)//2)*arr[i]
        
        
        return sumval
            
        """
        0,1,2,3...i,i+1,i+2...n
        
        0=k
        1=ceil((1-0)/2)+ ceil(n-1/2) 
        2=ceil(2/2)+ ceil(n-1/2)
        
        0 1 2
        3 4 5
        
        
        
        
        n
        K= ceil(n/2) 
        even = n- odd
        
        
        """
            
        
            
            
            
        
        
        