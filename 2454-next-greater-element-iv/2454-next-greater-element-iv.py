class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        
        
        greaterFound=[]
        notFound=[]
        ans=[-1]*len(nums)
        for i,val in enumerate(nums):
            
            while greaterFound and nums[greaterFound[-1]]<val:
                ans[greaterFound.pop()]=val
            temp=[]
            while notFound and nums[notFound[-1]]<val:
                temp.append(notFound.pop())
            
            greaterFound+=temp[::-1]
            notFound.append(i)
        
        return ans
        