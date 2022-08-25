class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        rc=Counter(ransomNote)
        mc=Counter(magazine)
        
        for c in rc:
            
            if mc[c]<rc[c]:
                return False
            
        return True
            