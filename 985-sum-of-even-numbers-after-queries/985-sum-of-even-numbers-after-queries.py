class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        
        evenSum=0
        oddSum=0
        
        evenSet=set()
        
        
        for i,val in enumerate(nums):
            
            if val&1:
                oddSum+=val
            else:
                evenSum+=val
                evenSet.add(i)
        
        ans=[]
        for val,i in queries:
            cur=nums[i]
            if cur&1:
                if val&1:
                    nums[i]+=val
                    evenSum+=nums[i]
                    oddSum-=cur
                else:
                    oddSum+=val
                    nums[i]+=val
            else:
                if val&1:
                    nums[i]+=val
                    evenSum-=cur
                    oddSum+=nums[i]
                else:
                    evenSum+=val
                    nums[i]+=val
            ans.append(evenSum)
        
        return ans
            
            
            
        