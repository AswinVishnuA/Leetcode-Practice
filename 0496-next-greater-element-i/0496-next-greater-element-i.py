class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d=defaultdict(int)
        notFound=[]
        ans=[-1]*len(nums2)
        for i,val in enumerate(nums2):
            d[val]=i
            
            while notFound and nums2[notFound[-1]]<val:
                ans[notFound.pop()]=val
            
            notFound.append(i)
        
        res=[]
        
        for num in nums1:
            res.append(ans[d[num]])
        
        return res
            
            
        