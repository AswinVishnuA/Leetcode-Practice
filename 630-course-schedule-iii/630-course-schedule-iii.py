
# def solve(curtime,cs,i,dp):
#         if i==len(cs):
#             return 0
        
#         dp_str=str(curtime)+"|"+str(i)
#         if dp_str in dp:
#             return dp[dp_str]
        
#         if curtime+cs[i][0]<=cs[i][1]:
#             dp.update({dp_str:max(1+solve(curtime+cs[i][0],cs,i+1,dp),solve(curtime,cs,i+1,dp))})
#             return dp[dp_str]
        
#         dp.update({dp_str:solve(curtime,cs,i+1,dp)})
#         return dp[dp_str]
        
class Solution:
    
        
    def scheduleCourse(self, cs: List[List[int]]) -> int:
        cs.sort(key=lambda x:x[1])
        # curtime=0
        # dp=dict()
        # # print(dp)
        # return solve(curtime,cs,0,dp)
        cur=0
        pq=[]
        for dur,day in cs:
            
            cur=cur+dur
            heapq.heappush(pq,-dur)
            
            if cur>day:
                cur+=heapq.heappop(pq)
        
        return len(pq)
            
            
        