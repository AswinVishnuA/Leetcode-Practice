class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        length=len(scores)
        
        pair=[]
        for i in range(length):
            pair.append([ages[i],scores[i]])
        
        pair.sort()
        '''
        dp[i]=
        
        '''
        
        
        dp=[0]*length
        
        dp[0]=pair[0][1]
        
        for i in range(1,length):
            dp[i]=pair[i][1]
            for j in range(i):
                if pair[i][1]>=pair[j][1]:
                    dp[i]=max(dp[i],pair[i][1]+dp[j])
        
        return max(dp)
                
        
        