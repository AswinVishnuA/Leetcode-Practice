class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        chars =  set("a b c d e f g h i j k l m n o p q r s t u v w x y z".split())
        
        s=set(list(sentence))
        
        return chars==s
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        