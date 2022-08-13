class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        
        s_len=len(s)
        word_len=len(words)
        sword_len=len(words[0])
        sub_size=word_len*sword_len
        ans=[]
        d=Counter(words)
        
        
        def sliding(left):
            
            cur_count=defaultdict(int)
            
            word_count=0
            
            excess_word=False
            
            for right in range(left,s_len,sword_len):
                
                if right+sword_len>s_len:
                    break
                
                
                word=s[right:right+sword_len]
                
                if word in d:
                    
                    while right-left==sub_size or excess_word:
                        
                        left_word=s[left:left+sword_len]
                        
                        left+=sword_len
                        
                        cur_count[left_word]-=1
                        
                        if cur_count[left_word]==d[left_word]:
                            excess_word=False
                        else:
                            word_count-=1
                    
                    cur_count[word]+=1
                    if cur_count[word]<=d[word]:
                        word_count+=1
                    else:
                        excess_word=True
                    
                    if word_count==word_len and not excess_word:
                        ans.append(left)
                else:
                    
                    cur_count=defaultdict(int)
                    word_count=0
                    excess_word=False
                    left=right+sword_len
                    
                    
        
        
        
        for i in range(sword_len):
            sliding(i)
        
        
        
        return ans
                
        
        
        
        
        
        
        
        """
        
        s = "barsdfoobarthefoobarthefoobarman",
        words = ["bar","foo","the"]
        
        
        """