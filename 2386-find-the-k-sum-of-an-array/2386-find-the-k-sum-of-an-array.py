class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        
        n=len(nums)
        maxSum=sum(max(nums[i],0) for i in range(n))
        
        absArr=sorted([abs(nums[i]) for i in range(n)])
        
        minHeap=[maxSum]
        
        maxHeap=[[-maxSum+absArr[0],0]]
        
        for i in range(k-1):
            
            cur,idx=heappop(maxHeap)
            
            heappush(minHeap,-cur)
            
            if idx+1<n:
                
                heappush(maxHeap,[cur-absArr[idx]+absArr[idx+1],idx+1])
                heappush(maxHeap,[cur+absArr[idx+1],idx+1])
        
        return minHeap[0]

            
            
            