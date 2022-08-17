class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        d={}
        i=0
        for c in "abcdefghijklmnopqrstuvwxyz":
            d[c]=morse[i]
            i+=1
        
        s=set()
        for word in words:
            code=""
            for c in word:
                code+=d[c]
            
            s.add(code)
        
        return len(s)
                
        