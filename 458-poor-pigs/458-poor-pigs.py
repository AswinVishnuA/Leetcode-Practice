class Solution:
    def poorPigs(self, b: int, mtd: int, mtt: int) -> int:
        
        count=0
        while (mtt//mtd +1)**count<b:
            count+=1
        
        return count
        