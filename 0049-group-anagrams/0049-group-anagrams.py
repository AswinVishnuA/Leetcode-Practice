class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d=defaultdict(list)
        
        for word in strs:
            
            c=Counter(word)
            # print(c["a"])
            key = [c[char] for char in "abcdefghijklmnopqrstuvwxyz"]
            
            d[tuple(key)].append(word)
        # print(d)
        ans=[]
        for key in d:
            ans.append(d[key])
            
        
        return ans
            
            
                
                
                
        
        
        