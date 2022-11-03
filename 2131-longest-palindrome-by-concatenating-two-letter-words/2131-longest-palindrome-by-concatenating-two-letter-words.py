class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        count=Counter(words)
        
        maxLen=0
        mid=""
        left=""
        flag=True
        print(count)
        for word in count:
            reversedWord=word[::-1]
            
            if flag and reversedWord==word and count[word]%2==1:
                mid=word
                count[word]-=1
                flag=False
            
            if count[reversedWord]>0:
                
                if reversedWord!=word:                
                    left+=word*min(count[word],count[reversedWord])
                    temp=min(count[word],count[reversedWord])
                    count[word]-=temp
                    count[reversedWord]-=temp
                elif count[word]>1:
                    left+=word*min(count[word]//2,count[reversedWord]//2)
                    count[word]-=min((count[word]//2)*2,(count[reversedWord]//2)*2)
                    
        print(left,mid,left[::-1])
        return len(left)*2 + len(mid)
                
                
                
        
        