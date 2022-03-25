class Solution:
    def combinationSum(self, cand: List[int], tar: int) -> List[List[int]]:
        
        ans=[]
        cand.sort()
        def solve(idx,tr,temp):
            
            
            if tr==0:
                ans.append(temp)
                return
            
            
            if idx>=len(cand) or cand[idx]>tr:
                return
            
            for i in range(idx,len(cand)):
                solve(i,tr-cand[i],temp+[cand[i]])
            # solve(idx+1,tr,temp)
            # temp.append(cand[idx])
            # solve(idx,tr-cand[idx],temp)
            # temp.pop()
        solve(0,tar,[])
        return ans
    
            
        