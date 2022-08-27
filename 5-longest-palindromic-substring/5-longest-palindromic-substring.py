class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n=len(s)
        ans=1
        leftIdx=0
        rightIdx=0
        for i in range(n):
            
            left=i
            right=i+1
            evenLen=0
            while left>=0 and right<n and s[left]==s[right]:
                evenLen+=2
                left-=1
                right+=1
            if evenLen>ans:
                ans=evenLen
                leftIdx=left+1
                rightIdx=right-1
            
            left=i-1
            right=i+1
            oddLen=1
            while left>=0 and right<n and s[left]==s[right]:
                oddLen+=2
                left-=1
                right+=1
                
            if oddLen>ans:
                ans=oddLen
                leftIdx=left+1
                rightIdx=right-1
            
            
        return s[leftIdx:rightIdx+1]
                
        